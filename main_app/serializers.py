from rest_framework import serializers
from .models import Thought, Recurrence, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ThoughtSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Thought
        fields = '__all__'

    tags = TagSerializer(many=True, read_only=True)


class RecurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurrence
        fields = '__all__'