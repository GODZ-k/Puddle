from django.urls import path
from .views import *
urlpatterns = [
    path("<id>",detail,name="detail"),
    path('delete/<id>',delete_item,name="delete"),
    path("update/<id>",update_item,name="update"),
    # path("do_update/<id>",do_update,name="do_update")
]
