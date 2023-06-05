from django.shortcuts import render
from .models import Product
# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, "menu/home.html", {"products": products})

def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, "menu/product.html", {"product": product})