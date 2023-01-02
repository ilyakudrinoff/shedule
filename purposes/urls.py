from django.urls import path

from . import views

app_name = 'purposes'

urlpatterns = [
    path('', views.index, name='index'),
    path('purposes/', views.purposes, name='purposes'),
    path('purposes/<purpose_pk>/', views.purpose, name='purpose'),
    path('purposes/create', views.purpose_create, name='purpose_create'),
    path('purposes/<purpose_pk>/task/create', views.task_create, name='task_create'),
    path('purposes/<purpose_pk>/edit/', views.purpose_edit, name='purpose_edit'),
    path('purposes/<purpose_pk>/tasks/<task_pk>', views.task, name='task'),
    path('purposes/<purpose_pk>/tasks/<task_pk>/edit', views.task_edit, name='task_edit'),
]
