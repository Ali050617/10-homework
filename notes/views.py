from django.shortcuts import render, redirect, get_object_or_404
from .models import Notes



def home(request):
    return render(request, 'index.html')



def notes_list(request):
    notes = Notes.objects.all()
    ctx = {'notes': notes}
    return render(request, 'notes/notes-list.html', ctx)

def notes_create (request):
    if request.method == 'POST':
        note_title = request.POST.get('note_title')
        content = request.POST.get('content')
        if note_title and content:
            Notes.objects.create(
                note_title=note_title,
                content=content,
            )
            return redirect('notes:list')
    return render(request, 'notes/notes-form.html')



def notes_detail(request, pk):
    notes = get_object_or_404(Notes, pk=pk)
    ctx = {'notes': notes}
    return render(request, 'notes/detail.html', ctx)



def notes_update(request, pk):
    notes = get_object_or_404(Notes, pk=pk)
    if request.method == 'POST':
        note_title = request.POST.get('note_title')
        content = request.POST.get('content')
        if note_title and content:
            notes.note_title = note_title
            notes.content = content
            notes.save()
            return redirect(notes.get_detail_url())
    ctx = {'notes': notes}
    return render(request, 'notes/notes-form.html', ctx)



def notes_delete(request, pk):
    notes = get_object_or_404(Notes, pk=pk)
    notes.delete()
    return redirect('notes:list')