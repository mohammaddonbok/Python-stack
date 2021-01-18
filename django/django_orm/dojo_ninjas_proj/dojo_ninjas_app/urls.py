from django.contrib import admin
from django.urls import path ,include
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.root),
    path('addDojo', views.insertDojos),
    path('addNinja', views.insertNinja),
    path('delete', views.deleteNinja)
]