from django.urls import path
from .views import *
urlpatterns = [
    path("<id>",detail,name="detail")
]
