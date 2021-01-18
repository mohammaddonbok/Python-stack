from django.shortcuts import render
def index(request):
    return render(request,"survey.html")

def display(request):
    context ={
    "n": request.GET['name'],
    "lo": request.GET['locat'],
    "la": request.GET['lang'],
    "c": request.GET['text'],
    }
    return render(request,"submit.html",context)