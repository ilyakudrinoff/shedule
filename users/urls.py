from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logged_out, name='logged_out'),
]
