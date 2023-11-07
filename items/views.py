from django.shortcuts import render
from items.models import *

# Create your views here.
def detail(request,id):
    item=Item.objects.get(id=id)
    return render(request,"detail.html",{'item':item})