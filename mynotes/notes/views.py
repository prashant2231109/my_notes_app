from django.shortcuts import render,redirect,get_object_or_404
from .models import Note
from django.http import HttpResponse
from .forms import NoteForm
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
