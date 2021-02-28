from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=255, default="Brak opisu")
    body = RichTextField(blank=True, null=True)
    miniature = models.FileField(upload_to="image/%y/%m", default="defBlog.png")
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default="brak kategorii")
    blog_likes = models.ManyToManyField(User, related_name='blog_post')

    def __str__(self):
        return str(self.title) + ' | ' + str(self.author)

    class Meta:
        ordering = ['date_added']
