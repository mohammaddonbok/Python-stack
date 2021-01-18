from django.urls import path
from . import views
urlpatterns = [
    # path('', views.index),
    path('', views.display),
    path('add', views.add),
]