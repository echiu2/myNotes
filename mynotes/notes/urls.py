from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.note_list, name='note_list'),
    path('notes/<slug:slug>/', views.note_content, name='note_content'),
    path('notes/<slug:slug>/create_subNote/', views.create_subNote, name='create_subNote'),
    path('notes/<slug:slug>/update_note/', views.update_note, name='update_note'),
    path('notes/<slug:slug>/<slug:slug2>/', views.subNote_content, name='subNote_content'),
]