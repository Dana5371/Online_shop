from django.db import models
from ckeditor.fields import RichTextField

class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    text = RichTextField()

    def __str__(self):
        return self.title

class AboutUsImage(models.Model):
    image = models.ImageField(upload_to = 'about', blank = True, null = True)
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='about_us_images')
