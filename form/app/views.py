from django.shortcuts import render,redirect
from .models import User
from .forms import Userreg
# Create your views here.

def show(request):
    data = Userreg()
    return render(request,'index.html',{'form':data})

def add(request):
    if request.method =="POST":
        data = Userreg(request.POST)
        if data.is_valid():
            na = data.cleaned_data['name']
            em = data.cleaned_data['email']
            pa = data.cleaned_data['password']
            User.objects.create(Name=na,Email=em,Password=pa)
            data = Userreg()
            return render(request,'index.html',{'form':data})
        
def table(request):
    data = User.objects.all()
    return render(request,'table.html',{'data':data})

def delete(request,uid):
    User.objects.filter(id=uid).delete()
    return redirect('/table/')
    
def update(request,uid):
    res = User.objects.get(id=uid)
    data = Userreg()
    return render(request,'update.html',{'uid':res,'data':data})

def ur(request):
    if request.method =="POST":
        data = Userreg(request.POST)
        if data.is_valid():
            hi = request.POST['hide']
            na = data.cleaned_data['name']
            em = data.cleaned_data['email']
            pa = data.cleaned_data['password']
            User.objects.filter(id=hi).update(Name=na,Email=em,Password=pa)
            return redirect('/table/')