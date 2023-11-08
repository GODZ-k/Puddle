from django.shortcuts import render,redirect
from items.models import Catagories,Item
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here

def home(request):
    items=Item.objects.all()
    catagory=Catagories.objects.all()

    data={
        "items":items,
        "catagory":catagory
    }
    return render(request, "index.html",data)

def login_user(request):
    if request.method == "POST":
        email=request.POST.get("email")
        password=request.POST.get("password")

        user_data=User.objects.filter(username=email)
        if not user_data.exists():
            messages.error(request,"Please enter valid email")
            return redirect("/login/")
        else:
            user=authenticate(username=email, password=password)
            if not user:
                messages.error(request,"Please enter valid password")
                return redirect("/login/")
            else:
                login(request,user)
                return redirect("/")
    return render(request,'login.html')

def signup_user(request):
    if request.method == 'POST':
        name=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")


        user_email=User.objects.filter(username=email)
        if user_email.exists():
            messages.error(request,"User already exists")
            return redirect("/signup/")

        user=User.objects.create(
            username=email,
            first_name=name
            # email=email
         )
        user.set_password(password)
        user.save()
        messages.success(request,"Account created successfully")
        return redirect("/login/")

    return render(request,'signup.html')

def logout_user(request):
    logout(request)
    return redirect("/login/")