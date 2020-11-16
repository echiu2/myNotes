from django.shortcuts import render, HttpResponse
from .forms import createNote

# Create your views here.
def index(request):
    form = createNote()
    context = {'form':form}
    return render(request, 'notes/notes.html', context)
