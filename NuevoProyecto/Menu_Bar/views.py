from django.shortcuts import render, HttpResponse
from .models import Product
# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, "Menu_Bar/home.html", {"products": products})

def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, "Menu_Bar/product.html", {"product": product})