from django.shortcuts import render

from rest_framework import generics
from .models import Folder, Image
from .serializers import FolderSerializer, ImageSerializer

class FolderListCreateView(generics.ListCreateAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

    class ImageListCreateView(generics.ListCreateAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        folder_id = self.kwargs['folder_id']
        return Image.objects.filter(folder_id=folder_id)

    def perform_create(self, serializer):
        folder_id = self.kwargs['folder_id']
        folder = Folder.objects.get(id=folder_id)
        serializer.save(folder=folder)