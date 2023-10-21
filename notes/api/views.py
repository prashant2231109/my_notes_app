from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer 
from ..models import Note


@api_view(['GET'])
def notes(request):
    note = Note.objects.all()
    serializer = NoteSerializer(note, many=True)
    return Response(serializer.data)
 
@api_view(['POST'])
def create(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
 
@api_view(['GET'])
def read(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note)
    return Response(serializer.data)


@api_view([ 'PUT'])
def update(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view([ 'GET'])
def delete(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Deleted")