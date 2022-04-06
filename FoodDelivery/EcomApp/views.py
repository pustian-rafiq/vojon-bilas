from django.shortcuts import render
from EcomApp.models import Setting
from Product.models import Product

#For Admin: email:rafiqul.pust.cse@gmail.com pass:rafiq123
# Create your views here.

def Home(request): 
    setting = Setting.objects.get(id=1)
    slider_images = Product.objects.all().order_by("id")[:2]
    latest_products = Product.objects.all().order_by("-id")
    products = Product.objects.all()
    
    context={
        'setting': setting,
        'slider_images': slider_images,
        "latest_products": latest_products,
        "products": products,
        }
    return render(request, 'home.html',context)
