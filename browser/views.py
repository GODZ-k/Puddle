from django.shortcuts import render
from items.models import *
from django.db.models import Q


# Create your views here.
def index(request):
    items=Item.objects.filter(sold_out=False)
    category=Catagories.objects.all()
    if request.method == 'GET':
        search=request.GET.get('search','')
        if search != None:
            items=Item.objects.filter(
                Q(name__icontains=search)|
                Q(price__icontains=search)|
                Q(description__icontains=search)|
                Q(catagories__name__icontains=search)
            )

    data={
        "items": items,
        "search":search,
        "category": category
        # "item":item
    }
    return render(request,'browser.html',data)