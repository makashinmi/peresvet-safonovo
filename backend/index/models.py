from django.db import models

# Create your models here.


class Post(models.Model):
    text = models.TextField()
    thumbnail = models.FileField(upload_to='posts/')

    def __str__(self):
        return self.text


class Photo(models.Model):
    file = models.FileField(upload_to='photos/')

    def __str__(self):
        return self.file.name


class Slider_Photo(models.Model):
    file = models.FileField(upload_to='slider/')

    def __str__(self):
        return self.file.name


class Trainer(models.Model):
    fullname = models.CharField(max_length=64)
    photo = models.FileField(upload_to='trainers/')
    description = models.TextField()

    def __str__(self):
        return self.fullname
