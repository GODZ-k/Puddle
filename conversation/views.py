from django.shortcuts import render
from items.models import Item

# Create your views here.
def new_conversation(request):
    return render(request, 'conversation.html')
