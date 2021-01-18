from django.shortcuts import render,redirect
from .models import User    
# show all of the data from a table
def display(request):
    context = {
    	"all_users": User.objects.all()
    }
    return render(request, "user.html", context)

def add(request):
    f_n=request.POST['first_name']
    l_n=request.POST['first_name']
    ag=request.POST['age']
    em = request.POST['email']
    User.objects.create(first_name=f_n,last_name=l_n,email=em,age=ag)
    return redirect('/')
# Create your views here.
