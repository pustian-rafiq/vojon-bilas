from django.shortcuts import render
#email:rafiqul.pust.cse@gmail.com pass:rafiq123
# Create your views here.
def Home(request): 
    context={}
    return render(request, 'home.html',context)
