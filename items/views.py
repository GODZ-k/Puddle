from django.shortcuts import render,redirect
from .models import *
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
    deleted_item=Item.objects.get(id=id , created_by=request.user)
    deleted_item.delete()

    return redirect("/dashboard/")

# update item
@login_required
def update_item(request,id):
    data={
        'updated_item':Item.objects.get(id=id, created_by=request.user),
        }
    return render(request,'update.html',data)
@login_required
def do_update(request,id):
    updated_item=Item.objects.get(id=id, created_by=request.user)

    if request.method == 'POST':
        updated_name=request.POST.get("name")
        updated_desc=request.POST.get("description")
        updated_price=request.POST.get("price")
        updated_img=request.FILES.get("image")
        sold_out = "sold_out" in request.POST  # Check if the checkbox is selected


#
        try:
            updated_price = float(updated_price)
        except ValueError:
            updated_item.price = 0.0

        updated_item.name=updated_name
        updated_item.description=updated_desc
        updated_item.price = updated_price
        updated_item.sold_out = sold_out


        if updated_img:
         updated_item.image=updated_img

        # print(updated_name)
        updated_item.save()

        return redirect("detail", id=updated_item.id)

    # return render(request, 'update.html', {'updated_item': updated_item})

