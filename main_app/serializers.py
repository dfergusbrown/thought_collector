from rest_framework import serializers
from .models import Thought, Recurrence

class ThoughtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thought
        fields = '__all__'

class RecurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurrence
        fields = '__all__'