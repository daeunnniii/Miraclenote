from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'addnote'

urlpatterns = [
    path('', views.index, name='index'),
    path('saveNote/', views.saveNote, name='savenote'),
    path('myNote/<int:note_id>/', views.result, name='result'),
    path('myNote/<int:note_id>/vis/', views.view_network, name='vis'),
    path('editnote/<int:note_id>/', views.addnote_save, name='addnote_save'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
