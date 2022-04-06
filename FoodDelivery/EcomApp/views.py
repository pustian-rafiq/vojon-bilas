from django.shortcuts import render
from EcomApp.models import Setting
from Product.models import Product

#For Admin: email:rafiqul.pust.cse@gmail.com pass:rafiq123
# Create your views here.

def Home(request): 
    setting = Setting.objects.get(id=1)
    slider_images = Product.objects.all().order_by("id")[:2]
    context={
        'setting': setting,
        'slider_images': slider_images,
        }
    return render(request, 'home.html',context)
