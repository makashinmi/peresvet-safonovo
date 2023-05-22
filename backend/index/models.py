from django.db import models

# Create your models here.


class Post(models.Model):
    text = models.TextField()
    thumbnail = models.FileField(upload_to='posts/')
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Блог'

    def __str__(self):
        return self.text


class Photo(models.Model):
    file = models.FileField(upload_to='photos/')

    class Meta:
        verbose_name = 'Фото галереи'
        verbose_name_plural = 'Галерея'

    def __str__(self):
        return self.file.name


class Slider_Photo(models.Model):
    file = models.FileField(upload_to='slider/')

    class Meta:
        verbose_name = 'Фото слайдера'
        verbose_name_plural = 'Слайдер'

    def __str__(self):
        return self.file.name


class Trainer(models.Model):
    fullname = models.CharField(max_length=64)
    photo = models.FileField(upload_to='trainers/')
    description = models.TextField()

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'

    def __str__(self):
        return self.fullname


class Address(models.Model):
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.address[:50]
