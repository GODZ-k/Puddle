from django.shortcuts import render
from items.models import *
from django.db.models import Q


# Create your views here.
def index(request):
    items=Item.objects.filter(sold_out=False)
    category=Catagories.objects.all()

    if request.method == 'GET':
        search=request.GET.get('search','')
        category_name=request.GET.get('category', '')

        if search != None:
            items=Item.objects.filter(
                Q(name__icontains=search)|
                Q(price__icontains=search)|
                Q(description__icontains=search)
                # Q(categories__name__icontains=search)
            )
        if category_name:
         items=items.filter(catagories__name=category_name)

    data={
        "items": items,
        "search":search,
        "category": category,
        "category_name":category_name
        # "item":item
    }
    return render(request,'browser.html',data)