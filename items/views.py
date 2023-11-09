from django.shortcuts import render
from items.models import *

# Create your views here.
#  Product detail ---------------------------
def detail(request,id):
    item=Item.objects.get(id=id)
    related_item=Item.objects.filter(catagories=item.catagories,sold_out=False).exclude(id=id)[0:10]
    data={
        "item":item,
        "related_item":related_item
    }
    return render(request,"detail.html",data)

