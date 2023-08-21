from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Note
from .forms import AddNoteForm
from django.contrib.auth.decorators import login_required

@login_required
def notes(request):
    notes = Note.objects.order_by("updated_at").filter(user=request.user).all()
    form = AddNoteForm()
    context = {
        "notes": notes,
        "form": form
    }     
    return render(request,"home.html",context)

@login_required
def create(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('notes')
@login_required
def destroy(request,noteId):
    note = Note.objects.get(pk=noteId)
    note.delete()
    return redirect('notes')

@login_required
def update(request,noteId):
    if request.method == 'POST':
        note = Note.objects.get(pk=noteId)
        form = AddNoteForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')
        
