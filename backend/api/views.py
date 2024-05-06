from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics #automatically creating new user or forms
from .serializers import UserSerializer, NoteSerializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note
# Create your views here.
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user) #you can only view the notes written by you
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
        
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)



class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()       #list of all objects that we will be looking at while creating a user (make sure user doesnt already exists)
    serializer_class = UserSerializer             #tells this view what kind of data we need to accept to make a new user
    permission_classes = [AllowAny]     #specify who can actually call this (in this case it is anyone)
