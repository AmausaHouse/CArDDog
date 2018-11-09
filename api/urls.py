from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginview.as_view(), name="login"),
    path('signup', views.signupview.as_view(), name="singup")
]