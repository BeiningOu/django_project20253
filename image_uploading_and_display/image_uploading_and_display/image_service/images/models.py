from django.db import models

class Folder(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    folder = models.ForeignKey(Folder, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name

    @property
    def image_size(self):
        return self.image.size

    @property
    def image_width(self):
        from PIL import Image as PILImage
        img = PILImage.open(self.image.path)
        return img.width

    @property
    def image_height(self):
        from PIL import Image as PILImage
        img = PILImage.open(self.image.path)
        return img.height

    @property
    def is_grayscale(self):
        from PIL import Image as PILImage
        img = PILImage.open(self.image.path)
        return img.mode == 'L'