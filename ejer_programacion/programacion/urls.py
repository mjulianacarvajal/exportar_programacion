from django.urls import path
from . import views 

urlpatterns = [
    path('', views.programacion_list, name='programacion_list'),
    path('programacion_excel', views.programacion_excel, name='programacion_excel'),
    ]





