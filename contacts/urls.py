from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.contact_create, name='contact_create'),
    path('<contact_pk>', views.contact_card, name='contact_card'),
    path('<contact_pk>/edit', views.contact_edit, name='contact_edit'),
    path('<contact_pk>/delete', views.contact_delete, name='contact_delete'),
    path('<contact_pk>/meets', views.meets, name='meets'),
    path('<contact_pk>/meets/create', views.meet_create, name='meet_create'),
    path('meets/<meet_pk>/edit', views.meet_edit, name='meet_edit'),
    path('relationship/<relationship_pk>/edit', views.relationship_edit, name='relationship_edit'),
    path('<contact_pk>/relationship/create', views.relationship_create, name='relationship_create'),
    path('<contact_pk>/facts', views.facts, name='facts'),
    path('<contact_pk>/facts/create', views.fact_create, name='fact_create'),
    path('facts/<fact_pk>/edit', views.fact_edit, name='fact_edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
