from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404, reverse
from .forms import createNoteForm, subNoteForm
from django.contrib import messages
from .models import Note, sub_Note
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@login_required(login_url="/login/")
def index(request):
    # Used for submission: Check if request was performed using HTTP:"Post" -> if so, create form
    if request.method == "POST":
        form = createNoteForm(request.POST)
        if form.is_valid():
            # saves a new post instance from Note data
            form.save()

    # Instance of form
    form = createNoteForm()
    context = {'form':form}
    return render(request, 'notes/add_notes.html', context)

@login_required(login_url="/login/")
def note_list(request):
    list_notes = Note.objects.all()
    context = {'list_notes': list_notes}
    return render(request, 'notes/note_list.html', context)

@login_required(login_url="/login/")
def note_content(request, pk):
    if request.method == "POST":
        print('yes')
        note = Note.objects.get(id=pk)
        note.delete()
        return redirect('/notes')
        
    note = Note.objects.get(id=pk)
    #query all sub notes related to Note through foreign key relationships 
    sub_note = note.sub_note_set.all()
    context = {'note': note, 'sub_note': sub_note}
    return render(request, 'notes/note.html', context)

@login_required(login_url="/login/")
def create_subNote(request, pk=None):  
    note = get_object_or_404(Note, id=pk)
    if request.method == "POST":
        form = subNoteForm(request.POST or None, initial={'note':note})   
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('note_content', args=(pk,)))

    form = subNoteForm(request.POST or None, initial={'note':note})
    context = {'form': form, 'note': note}
    return render(request, 'notes/create_subNote.html', context)

@login_required(login_url="/login/")
def subNote_content(request, pk=None, pk2=None):
    subNote = sub_Note.objects.get(id=pk2)
    context = {'subNote': subNote}
    return render(request, 'notes/subNote.html', context)

@login_required(login_url="/login/")
def update_note(request, pk=None):
    # Query Note object with the parameter pk (primary key)
    # note = Note.objects.get(id=pk)
    note = get_object_or_404(Note, id=pk)
    #This is to get form of the note instance with data prefilled into the form 
    # (so more like an updateNote form)
    if request.method == "POST":
        # To update, pass instance of that existing note into the noteForm with the request
        form = createNoteForm(request.POST, instance=note)
        if form.is_valid():
            # update values
            note = form.save(commit=False)
            note.save()
            return HttpResponseRedirect(reverse('note_content', args=(pk,)))
    else:
        # data = {'title': note.subject_text, 'date': datetime.now(), 'note': note.note_field}
        form = createNoteForm(instance=note)

    context = {'form': form, 'note': note}
    return render(request, 'notes/update_notes.html', context)



