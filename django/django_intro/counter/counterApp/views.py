from django.shortcuts import render, HttpResponse, redirect

from django.http import JsonResponse
def root(request):
    if 'counter' in request.session:
        request.session['counter']+=1
    else:
        request.session['counter'] = 0
    return render(request, 'counter.html')
def destroy(request):
    del request.session['counter']
    return redirect('/')
def add(request):
    if 'counter' in request.session:
        request.session['counter']+=1
    else:
        request.session['counter'] = 0
    return redirect('/')
def add2(requset, val):
    requset.session['counter']+=val
    return redirect()

