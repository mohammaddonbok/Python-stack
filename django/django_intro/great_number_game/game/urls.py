from django.urls import path
from . import views
urlpatterns = [
    # path('', views.index),
    path('', views.root),
    path('play', views.game),
    path('again', views.destroy),
    path('score', views.score),
]