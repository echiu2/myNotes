from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.note_list, name='note_list'),
    path('notes/<str:pk>/', views.note_content, name='note_content')
]