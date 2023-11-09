from django.shortcuts import render
from items.models import *

# Create your views here.
def detail(request,id):
    item=Item.objects.get(id=id)
    related_item=Item.objects.filter(Catagories=item.Catagories,sold_out=False).exclude(id=id)[0:10]
    data={
        "item":item,
        "related_item":related_item
    }
    return render(request,"detail.html",data)