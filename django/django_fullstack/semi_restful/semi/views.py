from django.shortcuts import render ,redirect
from .models import *
from django.contrib import messages
def root(request):
    context={
        "all_shows": Shows.objects.all()
    }
    return render(request,"allShows.html",context)

def newShow(request):

    return render(request,"addShow.html")

def addShow(request):
    errors = Shows.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/new')
    else:
        Shows.objects.create(title=request.POST['title'],network=request.POST['network'],release_date=request.POST['date'], desc=request.POST['desc'])
    return redirect('/')

def displayShow(request,i):
    context={
        'show':Shows.objects.get(id=i)
    }

    return render(request,"displayShow.html",context)

def updateShow(request,i):
    u= Shows.objects.get(id=i)
    errors = Shows.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/edit/'+str(i))
    else:
        
        u.title=request.POST['title']
        u.network=request.POST['network']
        u.release_date=request.POST['date']
        u.desc=request.POST['desc']
        u.save()
    return redirect('/')

def editShow(request,i):
    context={
        "row":i
    }
    return render(request,"editShow.html",context)
def deleteRow(request,i):
    d=Shows.objects.get(id=i)
    d.delete()
    return redirect('/')
# Create your views here.
