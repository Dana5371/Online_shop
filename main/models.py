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
    title = models.CharField(max_length=55, verbose_name='Заголовок')
    description = RichTextField(verbose_name='Описание')

    def __str__(self):
        return self.title

#Помощь
class ImageHelp(models.Model):
    image = models.ImageField(upload_to='help_image')


class Help(models.Model):
    question = models.TextField(verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')


#Коллекция
class Collection(models.Model):
    image = models.ImageField(verbose_name='Фото')
    title = models.CharField(max_length=55,verbose_name='Название')

    def __str__(self):
        return self.title

#Слайдер
class Slider(models.Model):
    image = models.ImageField(upload_to='slider_image', null=True, verbose_name='Фото')
    field_link = models.CharField(max_length=150, blank=True, verbose_name='Ссылка')

    def __str__(self):
         return 'Some image or link'
2
#Обратный звонок
class BackCall(models.Model):
    STATUS = [
        ('yes', 'Да'),
        ('no', 'Нет'),
    ]
    name = models.CharField(max_length=155, verbose_name='Имя')
    number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number_of_phone = models.CharField(validators=[number_regex], max_length=14, unique=True, null=False, blank=False,verbose_name='Номер телефона')
    date_of_call = models.DateTimeField(verbose_name='Дата')
    status = models.CharField(choices=STATUS, default='no', max_length=155)

    def __str__(self):
        return self.name

#Товар
class Product(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='product',verbose_name='Коллекция')
    title = models.CharField(max_length=200,verbose_name='Заголовок')
    article = models.CharField(max_length=150,verbose_name='Артикль')
    old_price = models.IntegerField(verbose_name='Старая цена')
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, verbose_name='Скидка')
    new_price = models.IntegerField(blank=True,verbose_name='Новая цена')
    description = RichTextField(verbose_name='Описание')
    size = models.CharField(max_length=55, default='42-50',verbose_name='Размер')
    line_of_size = models.CharField(max_length=55,blank=True, null=True,verbose_name='Линейка')
    compound = models.CharField(max_length=155, verbose_name='Состав')
    amount = models.IntegerField(verbose_name='Кол-во')
    material = models.CharField(max_length=150, verbose_name='Материал')
    new = models.BooleanField(default=False, blank=True, null=True, verbose_name='Новинка')
    hit = models.BooleanField(default=False, blank=True, null=True, verbose_name='Хит продаж')
    favorite = models.BooleanField(default=False, blank=True, null=True, verbose_name='Избранные')

    def save(self):
        if self.discount != 0:
            price_with_discount = (self.old_price * self.discount) / 100
            self.new_price = self.old_price - price_with_discount
            super(Product, self).save()
        else:
            super(Product, self).save()
        self.line_of_size = (int(self.size[3:]) - int(self.size[0:2])) // 2
        super(Product, self).save()

    def __str__(self):
        return self.title


class ProductImageColor(models.Model):
    image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='Фото')
    color = RGBColorField()
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='Товары')


class User(models.Model):
    STATUS = [
        ('new', 'Новый'),
        ('issued', 'Оформлен'),
        ('cancelled', 'Отменен'),
    ]
    name = models.CharField(max_length=155, verbose_name='Имя')
    last_name = models.CharField(max_length=155, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Почта')
    number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number_of_phone = models.CharField(validators=[number_regex], max_length=14, unique=True, null=False,
                                       blank=False, verbose_name='Номер телефона')
    country = models.CharField(max_length=200, verbose_name='Страна')
    city = models.CharField(max_length=155, verbose_name='Город')
    date_of_order = models.DateTimeField(auto_now=True, verbose_name='Дата')
    status_of_order = models.CharField(choices=STATUS, default='new', max_length=155, verbose_name='Статус заказа')

    def __str__(self):
        return self.email






