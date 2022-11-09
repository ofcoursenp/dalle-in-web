from django.shortcuts import render,HttpResponse     
from . import main   
from .models import InputHm

# Create your views here.

def index(req):
    if req.POST.get('what'):
        what = req.POST.get('what')
        main.openloader(what=req.POST.get('what'))
        input = InputHm(name=what)
        input.save()

    return render(req,'index.html',{})

