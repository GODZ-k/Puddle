from django.urls import path
from .views import *
urlpatterns = [
    path("dashboard/",index , name="dashboard")

]
