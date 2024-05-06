from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}  # so that no one can read what te password is 

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        return user
    
class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id","title","content","created_at","author"]
        extra_kwargs = {"author": {"read_only":True}}