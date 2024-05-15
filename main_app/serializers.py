from rest_framework import serializers
from .models import Thought, Recurrence, Tag
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ThoughtSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)    
    
    class Meta:
        model = Thought
        fields = '__all__'



class RecurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurrence
        fields = '__all__'