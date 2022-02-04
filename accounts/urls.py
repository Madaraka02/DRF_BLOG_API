from django.urls import path
from .views import *
from knox import views as knox_views


urlpatterns = [
    path('login/', loginView),
    path('register/', registerView),
    path('logout/', knox_views.LogoutView.as_view()),
    path('logoutall/', knox_views.LogoutAllView.as_view()),
]