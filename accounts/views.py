from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import (
    LoginView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetCompleteView
)

from rest_framework.authtoken.models import Token as apiToken

from .models import customuser, userActivateToken

class customUserCreationForm(UserCreationForm):
    class Meta:
        model = customuser
        fields = [
            'email',
            'password1',
            'password2'
        ]
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        user.email = self.cleaned_data['email']
        user.save()

        activateToken = userActivateToken()
        activateToken.user_id = user
        activateToken.save()

        apiToken.objects.create(user = user)

        subject = "ユーザーを登録しました。 | lifelog"
        message = f'以下のリンクをクリックしてユーザー登録を完了してください。\nhttps://lifelog.piechika.com/accounts/activate/{activateToken.activate_token}/'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user.email]  # 宛先リスト
        send_mail(subject, message, from_email, recipient_list)
        
        return user

class customCreateView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = customUserCreationForm
    success_url = '/'

def activateUser(request, activateToken):
    print(activateToken)
    targetUser = userActivateToken.objects.activateUser(activateToken)
    print(targetUser)
    return HttpResponse(f'アクティベートトークン：{activateToken}<br>ユーザーemail：{targetUser.email}')

class customLoginView(LoginView):
    redirect_authenticated_user=True
    template_name='accounts/login.html'

class customPasswordChangeView(PasswordChangeView):
    redirect_authenticated_user=True
    template_name='accounts/passwordChange.html'
    success_url = 'accounts/passwordchanged/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        userToken = apiToken.objects.get(user_id=user.user_id)
        context['token'] = userToken.key
        return context

class customPasswordChangeDoneView(PasswordChangeDoneView):
    redirect_authenticated_user=True
    template_name='accounts/passwordChangeDone.html'

class customPasswordResetView(PasswordResetView):
    template_name='accounts/passwordReset.html'

class customPasswordResetDoneView(PasswordResetDoneView):
    template_name='accounts/passwordResetDone.html'

class customPasswordResetConfirmView(PasswordResetConfirmView):
    template_name='accounts/passwordResetConfirm.html'

class customPasswordResetSucceedView(PasswordResetCompleteView):
    template_name='accounts/passwordResetSucceed.html'