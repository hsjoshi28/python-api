from rest_framework import serializers
from .models import  Bugs

class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bugs
        fields = ['id', 'title', 'subject']