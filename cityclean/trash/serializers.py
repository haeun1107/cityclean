from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from .models import Trash
from user.models import User

class TrashListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trash
        fields = ['id', 'address', 'picture', 'information']

    def create(self, validated_data):
        user = User.objects.get(id=1) ###

class TrashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trash
        exclude = ['user']

    def create(self, validated_data):
        user = User.objects.get(id=1)
        trash = Trash.objects.create(
            address=validated_data['address'],
            picture=validated_data['picture'],
            information=validated_data['information'],
            latitude=validated_data['latitude'],
            longitude=validated_data['longitude'],
            user=user
        )
        return trash

class TrashListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trash
        fields = ['id', 'address', 'picture', 'latitude', 'longitude']

    def create(self, validated_data):
        user = User.objects.get(id=1) ###