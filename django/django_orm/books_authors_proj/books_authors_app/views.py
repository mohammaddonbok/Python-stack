from django.shortcuts import render,redirect
from .models import Book,Publisher
def root(request):
    context={
        "all_books":Book.objects.all()
    }
    return render(request,"addBook.html",context)
def authorPage(request):
    context={
        "all_authors":Publisher.objects.all()
    }
    return render(request,"addAuthor.html",context)
def bookPage(request):
    context={
        "all_books":Book.objects.all()
    }
    return render(request,"addBook.html",context)

def addBook(request):
    Book.objects.create(title=request.POST['title'],desc=request.POST['desc'])
    return redirect('/')

def addAuthor(request):
    Publisher.objects.create(first_name=request.POST['first_name'],
    last_name=request.POST['last_name'],
    notes=request.POST['note'])
    return redirect('/Authors')
def displayAuthor(request,i):
    author =Publisher.objects.get(id=i)
    Allbooks =Book.objects.all()
    context={
        "author":author,
        "books":author.books.all(),
        "Allbooks":Allbooks
    }
    return render(request,"authorData.html",context)
def assignBook(request,i):
    id=request.POST['selectBook']
    newBook=Book.objects.get(id=id)
    author=Publisher.objects.get(id=i)
    author.books.add(newBook)
    return redirect('/Authors')

def assignAuthor(request,i):
    id=request.POST['selectAuthor']
    newAuthor=Publisher.objects.get(id=id)
    book=Book.objects.get(id=i)
    book.publishers.add(newAuthor)
    return redirect('/Books')
def displayBook(request,i):
    book = Book.objects.get(id=i)
    Allauthors = Publisher.objects.all()
    context={
        "book":book,
        "authors":book.publishers.all(),
        "Allauthors":Allauthors
    }
    return render(request,"bookData.html",context)
# def displayBooks(request):
#     context={

#     }

#     return render(request,bookData.html,context)
#     author5=Publisher.objects.get(id=5)
# >>> author5.books.add(book2)

# Create your views here.
