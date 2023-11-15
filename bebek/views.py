from django.shortcuts import render
from .models import Menu

# Create your views here.
def index(req):
    data = Menu.objects.all()

    return render(req, "index.html", {"data" : data}) 