from django.shortcuts import render,redirect
from items.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    items=Item.objects.filter(created_by=request.user).distinct()
    return render(request, 'dashboard.html',{'items':items})


