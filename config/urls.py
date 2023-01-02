from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('purposes.urls', namespace='purposes')),
    path('auth/', include('users.urls', namespace='users')),
]
