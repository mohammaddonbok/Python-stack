from django.shortcuts import render,redirect
import random
def root(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0

    if 'user_state' not in request.session:
        request.session['user_state'] = 3
        
        
    
    if 'visits' not in request.session:
        request.session['name'] = []
        request.session['attempts'] = []
        request.session['visits'] = 0
        request.session['length'] = 0
    
    if 'user_num' not in request.session:
        request.session['cpu_num'] = random.randint(1, 100)
        print(request.session['cpu_num'])        
    print(request.session['cpu_num'])   
    return render(request,"game.html")

def game(request):
    if request.method == "POST":
        print("'%s'" % request.POST['user_state']   )
        if request.POST['user_state']:
            request.session['user_num'] = int(request.POST['user_state'])
        else:
            return redirect("/")
        
        if request.session['user_num'] < request.session['cpu_num']:
            request.session['user_state'] = 0
        
        if request.session['user_num'] > request.session['cpu_num']:
            request.session['user_state'] = 1

        if request.session['user_num'] == request.session['cpu_num']:
            request.session['user_state'] = 2
        
        if request.session['counter'] == 4:
            request.session['user_state'] = 4
        
        request.session['counter'] += 1
        return redirect("/")

def destroy(request):
    del request.session['user_num']
    del request.session['user_state']
    del request.session['cpu_num']
    del request.session['counter']
    del request.session['name']
    del request.session['attempts']
    del request.session['visits']
    return redirect("/")

def score(request):
    if request.method == "GET":
        request.session['visits'] += 1
        request.session['name'].append(request.GET['name'])
        request.session['attempts'].append(request.session['counter'])
        print(request.session['name'])
        request.session.save()
        request.session['length'] += 1
        print(f"Length is: {request.session['length']}")
        length = []
        for i in range(request.session['length']):
            length.append(i)
        print(length)
        context = {
            'username': request.session['name'],
            'attempts': request.session['attempts'],
            'range_list': length
        }
        return render(request, 'leader.html', context)
# Create your views here.
