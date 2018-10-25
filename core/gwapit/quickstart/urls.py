from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'cats', views.CatViewSet, base_name='cats')
router.register(r'zombies', views.ZombieViewSet, base_name='zombies')

urlpatterns = [
    url(r'', include(router.urls))
]