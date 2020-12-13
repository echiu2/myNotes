from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.note_list, name='note_list'),
    path('notes/<str:pk>/', views.note_content, name='note_content'),
    path('notes/<str:pk>/create_subNote', views.create_subNote, name='create_subNote'),
    path('notes/<str:pk>/<str:pk2>', views.subNote_content, name='subNote_content'),
    path('notes/<str:pk>/update_note/', views.update_note, name='update_note')
]