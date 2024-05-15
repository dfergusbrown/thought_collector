from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import Thought, Recurrence, Tag
from .serializers import ThoughtSerializer, RecurrenceSerializer, TagSerializer, UserSerializer



# Create your views here.
class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the thought collector api home'}
        return Response(content)
    
class ThoughtList(generics.ListCreateAPIView):
    serializer_class = ThoughtSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Thought.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ThoughtDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ThoughtSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return Thought.objects.fitler(user=user)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

    def perform_update(self, serializer):
        thought = self.get_object()
        if thought.user != self.request.user:
            raise PermissionDenied({"message": "You do not have permission to edit this cat."})
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied({"message": "You do not have permission to delete this cat."})
        instance.delete()

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
    
#User

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': response.data
        })
    

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post (self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class VerifyUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = User.objects.get(username=request.user)
        refresh = RefreshToken.for_user(request.user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        })