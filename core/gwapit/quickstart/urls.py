from django.conf.urls import url,include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'zombie', views.ZombieViewSet)
router.register(r'cat', views.CatViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),

]
