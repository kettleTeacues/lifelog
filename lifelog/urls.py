from django.urls import path, re_path, include
from rest_framework import routers
from rest_framework.authtoken import views as drfAuthViews

from lifelog import views, api_views as Lifelog_api_views

router = routers.DefaultRouter()
router.register('', Lifelog_api_views.LifelogViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('listApi/', Lifelog_api_views.LifelogListAPIView.as_view(), name='listApi'),
    path('spanApi/', views.LifelogSpanApiView.as_view(), name='spanApi'),
    path('apitoken/', drfAuthViews.obtain_auth_token, name='apitoken'),
    path('aboutHtml', views.aboutApiView.as_view(), name='aboutHtml')
]
