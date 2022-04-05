from django.shortcuts import render
from EcomApp.models import Setting


#For Admin: email:rafiqul.pust.cse@gmail.com pass:rafiq123
# Create your views here.

def Home(request): 
    setting = Setting.objects.get(id=1)
    context={'setting': setting}
    return render(request, 'home.html',context)
