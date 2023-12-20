from rest_framework import serializers
from .models import Declaration
from user.models import User
from trashcan.models import TrashCans
from datetime import datetime

class DeclarationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Declaration
        exclude = ['user', 'trashCans', 'created_at']

    def create(self, validated_data):
        user = self.context['user']
        trashCans = self.context['trashCans']
        
        return Declaration.objects.create(user=user, trashCans=trashCans, created_at=datetime.now(), **validated_data)