from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from .models import TrashCans
from user.models import User

class TrashCanListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrashCans
        fields = ['id', 'address', 'picture', 'information']

    def create(self, validated_data):
        print("test")
        user = User.objects.get(id=1)

class TrashCanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrashCans
        exclude = ['user']
        
    def create(self, validated_data):
        user = User.objects.get(id=1) ###
        trashcan = TrashCans.objects.create(
            address=validated_data['address'],
            picture=validated_data['picture'],
            information=validated_data['information'],
            latitude=validated_data['latitude'],
            longitude=validated_data['longitude'],
            user=user
        )
        return trashcan


class TrashCansListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrashCans
        fields = ['id', 'address', 'picture', 'latitude', 'longitude']

    def create(self, validated_data):
        user = User.objects.get(id=1)
    