from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    threeLine = models.TextField(null=True)
    auth = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title =models.TextField()
    bodyBlog=models.TextField()
    date=models.TextField(null=True)
    image=models.ImageField(null=True)
    datetime=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    auth = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date=models.TextField(null=True)
