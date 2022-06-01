from django.db import models
from ckeditor.fields import RichTextField


#О нас
class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    text = RichTextField()

    def __str__(self):
        return self.title

class AboutUsImage(models.Model):
    image = models.ImageField(upload_to = 'about', blank = True, null = True)
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='about_us_images')


#Наши преимущества
class Benefit(models.Model):
    ICON = (
        ('png', 'png'),
        ('svg', 'svg'),
    )
    icon = models.CharField(choices=ICON, max_length=55)
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title


#Новости
class News(models.Model):
    image = models.ImageField(upload_to='news', blank=True, null=True)
    title = models.CharField(max_length=150)
    description = RichTextField()

    def __str__(self):
        return self.title


#Публичная оферта
class Oferro(models.Model):
    title = models.CharField(max_length=55)
    description = RichTextField()

    def __str__(self):
        return self.title

#Помощь
class ImageHelp(models.Model):
    image = models.ImageField(upload_to='help_image')

    def __str__(self):
        return self.image

class Question(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question

class Answer(models.Model):
    answer = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='help_answer')

    def __str__(self):
        return self.answer

