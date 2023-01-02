from django.urls import path

from . import views

app_name = 'purposes'

urlpatterns = [
    path('', views.index, name='index'),
    path('purposes/', views.purposes, name='purposes'),
    path('purposes/<purpose>/', views.purpose, name='purpose'),
    path('purposes/<purpose>/edit/', views.purpose_edit, name='purpose_edit'),
    path('purposes/<purpose>/tasks/<task>', views.task, name='task'),
    path('purposes/<purpose>/tasks/<task>/edit', views.task_edit, name='task_edit'),
]
