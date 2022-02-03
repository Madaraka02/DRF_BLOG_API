from rest_framework import routers
from django.urls import path
from .views import *


router = routers.DefaultRouter()
router.register('posts', PostViewSet)
urlpatterns = router.urls