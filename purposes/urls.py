from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'purposes'

urlpatterns = [
    path('', views.index, name='index'),
    path('purposes/create', views.purpose_create, name='purpose_create'),
    path('purposes/<purpose_pk>/edit', views.purpose_edit, name='purpose_edit'),
    path('purposes/<purpose_pk>/complete', views.purpose_complete, name='purpose_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
