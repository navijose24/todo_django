from django.urls import path
from . import views

urlpatterns=[
    path('', views.home),
    path('get/',views.get_tasks),
    path('add/',views.add_Tasks),
]