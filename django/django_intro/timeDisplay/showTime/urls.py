from django.urls import path, include           # import include
from . import views
urlpatterns = [
    path('', views.index)
]