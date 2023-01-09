from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic import CreateView

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

        subject = "題名"
        message = f'アクティベートリンク\nhttps://lifelog.piechika.com/accounts/activate/{activateToken.activate_token}/'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user.email]  # 宛先リスト
        send_mail(subject, message, from_email, recipient_list)
        
        return user


class customCreateView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = customUserCreationForm
    success_url = '/'

class customLoginView(LoginView):
    redirect_authenticated_user=True
    template_name='accounts/login.html'

class customPasswordChangeView(PasswordChangeView):
    redirect_authenticated_user=True
    template_name='accounts/passwordChange.html'
    success_url = 'accounts/passwordchanged/'

class customPasswordChangeDoneView(PasswordChangeDoneView):
    redirect_authenticated_user=True
    template_name='accounts/passwordChangeDone.html'

from django.http import HttpResponse
def mailtest(request):
    print('mailtest')
    subject = "題名"
    message = "本文\\nです"
    from_email = 'test.teacues@gmail.com'  # 送信者
    recipient_list = ["teacues@gmail.com"]  # 宛先リスト
    send_mail(subject, message, from_email, recipient_list)
    
    return HttpResponse("mailtest")

def activateUser(request, activateToken):
    print(activateToken)
    targetUser = userActivateToken.objects.activateUser(activateToken)
    print(targetUser)
    return HttpResponse(f'アクティベートトークン：{activateToken}<br>ユーザーemail：{targetUser.email}')