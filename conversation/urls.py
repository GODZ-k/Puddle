
from django.urls import path
from .views import *
urlpatterns = [
path("contact/",new_conversation,name="contact")
]
