from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import customCreateView, customLoginView, customPasswordChangeView, customPasswordChangeDoneView

urlpatterns = [
    path('signup/', customCreateView.as_view(), name='signup'),
    path('login/', customLoginView.as_view(), name='login'),
    path('password/', customPasswordChangeView.as_view(), name='password'),
    path('passwordchanged/', customPasswordChangeDoneView.as_view(), name='passwordchanged'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
