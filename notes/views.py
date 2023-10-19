from django.shortcuts import render,redirect,get_object_or_404
from .models import Note
from django.http import HttpResponse
from .forms import NoteForm
# from .forms import NoteSearchForm
# Create your views here.
def index(request):
    notes=Note.objects.all()
    return render(request,'notes/index.html',{'notes':notes})

def create(request):
    
    form = NoteForm(request.POST)
    # print("here")
    print(form.errors)
    if form.is_valid():
        form.save()
        return redirect('index') 
    
def delete_view(request,id):
    if request.method == "POST":
        note=get_object_or_404(Note,id=id)
        note.delete()
        return redirect('index')
    
def edit_view(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm(instance=note)
    print("Rendering Template")
    return render(request, 'notes/edit_view.html', { 'notes': note})

