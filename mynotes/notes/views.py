from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import createNoteForm
from django.contrib import messages
from .models import Note
from datetime import datetime

# Create your views here.
def index(request):
    # Used for submission: Check if request was performed using HTTP:"Post" -> if so, create form
    success = False
    if request.method == "POST":
        form = createNoteForm(request.POST)
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
        #saves notes into database
        note.save()

    # Instance of form
    form = createNoteForm()
    context = {'form':form}
    return render(request, 'notes/add_notes.html', context)

def note_list(request):
    list_notes = Note.objects.all()
    context = {'list_notes': list_notes}
    return render(request, 'notes/note_list.html', context)

def note_content(request, pk):
    note = Note.objects.get(id=pk)
    context = {'note': note}
    return render(request, 'notes/note.html', context)

def update_note(request, pk):
    note = Note.objects.get(id=pk)
    #This is to get form of the note instance with data prefilled into the form 
    # (so more like an updateNote form)
    if request.method == "POST":
        form = createNoteForm(request.POST, instance=note)
        if form.is_valid():
            # update values
            note.subject_text = form.cleaned_data['title']
            note.added_date = form.cleaned_data['date']
            note.note_field = form.cleaned_data['note']
            note.save()
            return redirect('/notes')
    else:
        data = {'title': note.subject_text, 'date': datetime.now(), 'note': note.note_field}
        form = createNoteForm(initial=data, instance=note)

    context = {'form': form, 'note': note}
    return render(request, 'notes/update_notes.html', context)