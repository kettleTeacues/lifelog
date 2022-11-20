from django.urls import path, include
from lifelog import views

urlpatterns = [
    path('', views.index, name='index'),
]
