from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()

class Profile(models.Model):
    image = models.ImageField(upload_to='media/')
    user = models.OneToOneField(USER,on_delete=models.CASCADE)
    info = models.TextField()


class Post(models.Model):

    STATUS_CHOICES = (('Published', 'Published'),
                      ('Draft', 'Draft'),)
    
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, max_length=255)
    image = models.ImageField(upload_to='media',blank=True)
    content = models.TextField()
    status = models.CharField(max_length=10, default='Draft', choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(USER, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_image_url(self, obj):
        return obj.image.url