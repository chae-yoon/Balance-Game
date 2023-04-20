from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    select1_content = models.CharField(max_length=20)
    select2_content = models.CharField(max_length=20)
    select1_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select1')
    select2_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select2')