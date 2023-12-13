from django.shortcuts import render,redirect
from items.models import Catagories,Item
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# new imports
from django.core.mail import EmailMessage,send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from .tokens import *
from puddle import settings

# Create your views here

#  Home page data --------------------------------
def home(request):
    items=Item.objects.all()
    catagory=Catagories.objects.all()

    data={
        "items":items,
        "catagory":catagory
    }
    return render(request, "index.html",data)

# add New item --------------------------------
@login_required
def additem(request):
    catagory=Catagories.objects.all()
    if request.method == "POST":
     product_catagory=request.POST.get('catagory')
     product_name=request.POST.get("name")
     product_description=request.POST.get("description")
     product_price=request.POST.get("price")
     product_image=request.FILES.get("image")
     user=request.user
     category=Catagories.objects.get(id=product_catagory)

     additem=Item(
         name=product_name,
         price=product_price,
         description=product_description,
         image=product_image,
         catagories=category,
         created_by=user
     )
     additem.save()
     return redirect("detail", id=additem.id)

    data={
        "catagory":catagory
    }
    return render(request,"additem.html",data)

#  Login user  --------------------------------
def login_user(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user_data=User.objects.filter(username=username)
        if not user_data.exists():
            messages.error(request,"Please enter valid email")
            return redirect("/login/")
        else:
            user=authenticate(username=username, password=password)
            if not user:
                messages.error(request,"Please enter valid password")
                return redirect("/login/")
            else:
                login(request,user)
                return redirect("/")
    return render(request,'login.html')

# sign up user --------------------------------

def signup_user(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")


        if User.objects.filter(username=username).exists():
           messages.error(request,"Username already exists")
           return redirect("/signup/")

        elif User.objects.filter(email=email).exists():
            messages.error(request,"Email already exists")
            return redirect("/signup/")

        elif len(username)>10:
            messages.error(request,"Username must be below 10 characters")

        elif not username.isalnum():
            messages.error(request,"Username must be Alphanumeric")
            return redirect("/signup/")

        else:
            user=User.objects.create(
            username=username,
            email=email
          )
            user.set_password(password)
            user.is_active=False
            user.save()
            messages.success(request,"Account created successfully")

            # Confirmation mail
            current_site=get_current_site(request)
            subject="Activate Your Puddle Account Now!"
            message=render_to_string("account_activation.html",{
                'name':user.username,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generatetoken.make_token(user),

            })

            semail=EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [user.email],

            )
            semail.fail_silently=True
            semail.send()
            return redirect("/login/")

    return render(request,'signup.html')

#  Log out user ----------------------------------

def logout_user(request):
    logout(request)
    return redirect("/login/")



def activate(request,uidb64,token):
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)
    except(ValueError,TypeError,User.DoesNotExist,OverflowError):
        user=None

    if user is not None and generatetoken.check_token(user,token):
        user.is_active=True
        user.save()
        login(request,user)
        return redirect("/")

    else:
        return render(request,"Activate_fail.html")