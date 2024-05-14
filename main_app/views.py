from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import Thought, Recurrence, Tag
from .serializers import ThoughtSerializer, RecurrenceSerializer, TagSerializer

# Create your views here.
class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the thought collector api home'}
        return Response(content)
    
class ThoughtList(generics.ListCreateAPIView):
    queryset = Thought.objects.all()
    serializer_class = ThoughtSerializer

class ThoughtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thought.objects.all()
    serializer_class = ThoughtSerializer
    lookup_field = 'id'

class RecurrenceList(generics.ListCreateAPIView):
    serializer_class = RecurrenceSerializer

    def get_queryset(self):
        thought_id = self.kwargs['thought_id']
        return Recurrence.objects.filter(thought_id = thought_id)
    
    def perform_create(self, serializer):
        thought_id = self.kwargs['thought_id']
        thought = Thought.objects.get(id=thought_id)
        serializer.save(thought=thought)

class RecurrenceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecurrenceSerializer
    lookup_field = 'id'

    def get_queryset(self):
        thought_id = self.kwargs['thought_id']
        return Recurrence.objects.filter(thought_id = thought_id)
    

#TAGS

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'id'


class AddTagToThought(APIView):
    def post(self, request, thought_id, tag_id):
        thought = Thought.objects.get(id=thought_id)
        tag = Tag.objects.get(id=tag_id)
        thought.tags.add(tag)
        return Response({'message': f'Tag {tag.name} added to Thought: {thought.name}'})
    
