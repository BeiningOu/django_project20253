from rest_framework import serializers
from .models import Folder, Image

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ['id', 'name', 'created_at']

class ImageSerializer(serializers.ModelSerializer):
    image_size = serializers.SerializerMethodField()
    image_width = serializers.SerializerMethodField()
    image_height = serializers.SerializerMethodField()
    is_grayscale = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['id', 'image', 'uploaded_at', 'image_size', 'image_width', 'image_height', 'is_grayscale']

    def get_image_size(self, obj):
        return obj.image_size

    def get_image_width(self, obj):
        return obj.image_width

    def get_image_height(self, obj):
        return obj.image_height

    def get_is_grayscale(self, obj):
        return obj.is_grayscale