from django.urls import path
from . import views

urlpatterns = [
    path("Login_user", views.Login_user, name = "Login"),
    path("logout_user", views.logout_user, name = "logout"),
    path("register_user", views.register_user, name = "register"),

]