from django.urls import path
from . import views

urlpatterns=[
    path('', views.root),
    path('new', views.newShow),
    path('addShow', views.addShow),
    path('show/<int:i>', views.displayShow),
    path('edit/<int:i>', views.editShow),
    path('editShow/<int:i>', views.updateShow),
    path('delete/<int:i>', views.deleteRow)
]