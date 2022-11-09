from django.shortcuts import render,HttpResponse     
from . import main   

# Create your views here.

def index(req):
    if req.POST.get('what'):
        main.openloader(what=req.POST.get('what'))
    return render(req,'index.html',{})

