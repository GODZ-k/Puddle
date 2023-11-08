
from django.urls import path
from .views import *
from items.views import *
urlpatterns = [
    path("", home , name="/"),
    path("logout/",logout_user,name="logout"),
    path("login/",login_user,name="login_user"),
    path("signup/",signup_user,name="signup_user"),

]
