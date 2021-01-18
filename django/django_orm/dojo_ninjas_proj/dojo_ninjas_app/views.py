from django.shortcuts import render,redirect
from .models import Dojos ,Ninjas
def root(request):
    context ={
        "Dojo":Dojos.objects.all(),
    }
    return render(request,"dojos.html",context)

def insertDojos(request):
    n=request.POST['name_dojo']
    c=request.POST['city']
    s=request.POST['state']
    Dojos.objects.create(name=n,city=c,state=s)
    return redirect('/')
def insertNinja(request):
    n=request.POST['first_name']
    l=request.POST['last_name']
    d=request.POST['select_dojo']
    Ninjas.objects.create(dojo=Dojos.objects.get(id=d),first_name=n,last_name=l)
    return redirect('/')

def deleteNinja(request):
    de=request.POST['btn']
    d=Dojos.objects.get(id=de)
    d.delete()
    return redirect('/')
# Create your views here.
