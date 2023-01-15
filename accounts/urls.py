from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.customCreateView.as_view(), name='signup'),
    path('activate/<activateToken>/',views.activateUser, name='activate'),
    path('login/', views.customLoginView.as_view(), name='login'),
    path('password/', views.customPasswordChangeView.as_view(), name='password'),
    path('passwordchanged/', views.customPasswordChangeDoneView.as_view(), name='passwordchanged'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', views.customPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', views.customPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', views.customPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', views.customPasswordResetSucceedView.as_view(), name='password_reset_complete'),
]
