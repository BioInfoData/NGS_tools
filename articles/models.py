from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    type = models.CharField(max_length=100, default="general")
    date = models.DateTimeField(auto_now_add=True)
    link = models.URLField(max_length=500,blank=True, default="#")
    thumb = models.ImageField(default="default.png", blank=True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Articles,on_delete=models.CASCADE,related_name='comments')
    name = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)