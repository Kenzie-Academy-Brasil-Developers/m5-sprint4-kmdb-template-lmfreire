from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("users/register/", views.UserRegisterView.as_view()),
    path('login/', views.UserLoginView.as_view()),
]
