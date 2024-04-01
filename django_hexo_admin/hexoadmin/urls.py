from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken import views as authtoken

router = DefaultRouter()
router.register('apitest', views.apitestViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth", authtoken.obtain_auth_token),
    path("register", views.RegisterAPI.as_view()),
    path("hexo_config", views.hexo_configAPI.as_view()),
    path("hexo_theme", views.hexo_themeAPI.as_view()),
    path("pull_hexo_theme", views.pull_hexo_themeAPI.as_view()),
    path("hexo_theme_config", views.hexo_theme_configAPI.as_view()),
    path("hexo_blogs", views.bolglistAPI.as_view()),
]
