from django.core.validators import RegexValidator
from django.db import models
from ckeditor.fields import RichTextField
from colorful.fields import RGBColorField

#О нас
class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    text = RichTextField()

    def __str__(self):
        return self.title


class AboutUsImage(models.Model):
    image = models.ImageField(upload_to='about', blank=True, null=True)
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='images')


#Наши преимущества
class Benefit(models.Model):

    icon = models.ImageField(upload_to='benefit')
    title = models.CharField(max_length=150)
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


class Help(models.Model):
    question = models.TextField()
    answer = models.TextField()


#Коллекция
class Collection(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title

#Слайдер
class Slider(models.Model):
    image = models.ImageField(upload_to='slider_image', null=True)
    field_link = models.CharField(max_length=150, blank=True)

    def __str__(self):
         return 'Some image or link'

#Обратный звонок
class BackCall(models.Model):
    STATUS = [
        ('yes', 'Да'),
        ('no', 'Нет'),
    ]
    name = models.CharField(max_length=155)
    number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number_of_phone = models.CharField(validators=[number_regex], max_length=14, unique=True, null=False, blank=False)
    date_of_call = models.DateTimeField()
    status = models.CharField(choices=STATUS, default='no', max_length=155)

    def __str__(self):
        return self.name

#Товар
class Product(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='product')
    title = models.CharField(max_length=200)
    article = models.CharField(max_length=150)
    old_price = models.IntegerField()
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)
    new_price = models.IntegerField(blank=True, null=True)
    description = RichTextField()
    line_of_size = models.CharField(max_length=55)
    compound = models.CharField(max_length=155)
    amount = models.IntegerField()
    material = models.CharField(max_length=150)
    new = models.BooleanField(default=False, blank=True, null=True)
    hit = models.BooleanField(default=False, blank=True, null=True)
    favorite = models.BooleanField(default=False, blank=True, null=True)

    def save(self):
        if self.discount != 0:
            price_with_discount = (self.old_price * self.discount) / 100
            self.new_price = self.old_price - price_with_discount
            super(Product, self).save()
        else:
            super(Product, self).save()

    def save(self):
        self.line_of_size = (int(self.line_of_size[3:]) - int(self.line_of_size[0:2])) // 2
        super(Product, self).save()

    def __str__(self):
        return self.title


class ProductImageColor(models.Model):
    image = models.ImageField(upload_to='product', blank=True, null=True)
    color = RGBColorField()
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')







