from django.urls import path
from . import views

urlpatterns=[
    path('', views.root),
    path('addBook',views.addBook),
    path('Authors',views.authorPage),
    path('Books',views.bookPage),
    path('addAuthor',views.addAuthor),
    path('displayAuthor/<int:i>', views.displayAuthor),
    path('assignAuthor/<int:i>', views.assignBook),
    path('assignBook/<int:i>',views.assignAuthor),
    path('displayBook/<int:i>',views.displayBook)
]
