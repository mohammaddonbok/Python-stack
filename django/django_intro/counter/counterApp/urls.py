from django.urls import path
from . import views
urlpatterns = [
    # path('', views.index),
    path('', views.root),
    path('destroy_session', views.destroy),
    path('add', views.add),
    path('insert', views.add2)
]