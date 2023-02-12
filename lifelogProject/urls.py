from django.contrib import admin
from django.urls import path, re_path, include
from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls.exceptions import NoReverseMatch

def base_view(request):
        return render(request, 'index.html')

urlpatterns = [
    path('', include('lifelog.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    re_path('^.*$', base_view)
 ]
