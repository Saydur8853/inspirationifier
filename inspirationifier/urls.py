
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from inspirationifierApp import views


router = routers.DefaultRouter()
router.register('watermark', views.ImageViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
