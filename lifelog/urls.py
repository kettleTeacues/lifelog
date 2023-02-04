from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as drfAuthViews

from lifelog import views, api_views as Lifelog_api_views

router = routers.DefaultRouter()
router.register('', Lifelog_api_views.LifelogViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('control/', views.control, name='control'),
    path('component/', views.component, name='component'),
    path('api/', include(router.urls)),
    path('list/', Lifelog_api_views.LifelogListAPIView.as_view()),
    path('apitoken/', drfAuthViews.obtain_auth_token, name='apitoken')
]
