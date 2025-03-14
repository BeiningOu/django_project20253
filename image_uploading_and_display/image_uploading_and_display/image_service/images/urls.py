from django.urls import path
from .views import FolderListCreateView, ImageListCreateView

urlpatterns = [
    path('folders/', FolderListCreateView.as_view(), name='folder-list-create'),
    path('folders/<int:folder_id>/images/', ImageListCreateView.as_view(), name='image-list-create'),
]