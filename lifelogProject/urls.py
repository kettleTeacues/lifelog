from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('lifelog.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('vue/', TemplateView.as_view(template_name='vue.html')),
 ]
