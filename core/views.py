from django.shortcuts import render
from items.models import Catagories,Item

# Create your views here

def home(request):
    items=Item.objects.all()
    catagory=Catagories.objects.all()

    data={
        "items":items,
        "catagory":catagory
    }
    return render(request, "index.html",data)