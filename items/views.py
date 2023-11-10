from django.shortcuts import render,redirect
from items.models import *
from django.contrib.auth.decorators import login_required

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


# delete item
@login_required
def delete_item(request,id):
    deleted_item=Item.objects.get(id=id,created_by=request.user)
    deleted_item.delete()

    return redirect("/dashboard/")

# update item
@login_required
def update_item(request,id):
    updated_item=Item.objects.get(id=id,created_by=request.user)
    data={
        'updated_item':updated_item,
        # 'catagory':Catagories.objects.all()
        }
    return render(request,'update.html',data)

def do_update(request,id):
    do_update_item=Item.objects.get(id=id)
    if request.method=='POST':
        
    return redirect("detail" ,id=do_update.id)