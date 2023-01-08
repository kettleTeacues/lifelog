from django.urls import path, include
from rest_framework import routers

from lifelog import views, api_views as Lifelog_api_views

router = routers.DefaultRouter()
router.register('', Lifelog_api_views.LifelogViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('control/', views.control, name='control'),
    path('api/', include(router.urls)),
    path('list/', Lifelog_api_views.LifelogListAPIView.as_view()),
]
