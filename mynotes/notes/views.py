from django.shortcuts import render, HttpResponse
from .forms import createNote
from django.contrib import messages
from .models import Note

# Create your views here.
def index(request):
    # Used for submission: Check if request was performed using HTTP:"Post" -> if so, create form
    success = False
    if request.method == "POST":
        form = createNote(request.POST)
        if form.is_valid():
            success = True
            # saves a new post instance from Note data
            # form.save()

    if success:
        messages.success(request, f'You have added a new note.')
        title = request.POST["title"]
        date = request.POST["date"]
        note = request.POST["note"]
        note = Note(subject_text=title, added_date=date, note_field=note)
        note.save()

    # Instance of form
    form = createNote()
    context = {'form':form}
    return render(request, 'notes/notes.html', context)
