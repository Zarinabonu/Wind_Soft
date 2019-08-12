from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200,null=True)
    description = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)


class Files(models.Model):
    file_user = models.ForeignKey('Post', on_delete=models.CASCADE)
    file = models.FileField(null=True)

# Create your models here.
