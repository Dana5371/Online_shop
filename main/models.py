from datetime import datetime

from django.core.validators import RegexValidator
from django.db import models
from ckeditor.fields import RichTextField
from colorful.fields import RGBColorField


class AboutUs(models.Model):
    """О нас"""
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    text = RichTextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class AboutUsImage(models.Model):
    """О нас"""
    image = models.ImageField(upload_to='about', blank=True, null=True)
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='images')


class Benefit(models.Model):
    """Наши преимущества"""
    icon = models.ImageField(upload_to='benefit')
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        verbose_name = 'Наши преимущества'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class News(models.Model):
    """Новости"""
    image = models.ImageField(upload_to='news', blank=True, null=True)
    title = models.CharField(max_length=150)
    description = RichTextField()

    class Meta:
        verbose_name = 'Новости'

    def __str__(self):
        return self.title


class Oferro(models.Model):
    """Публичная оферта"""
    title = models.CharField(max_length=55, verbose_name='Заголовок')
    description = RichTextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Публичная оферта'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ImageHelp(models.Model):
    """Фотография для помощи"""
    image = models.ImageField(upload_to='help_image')

    class Meta:
        verbose_name = 'Фотография для помощи'
        verbose_name_plural = verbose_name


class Help(models.Model):
    """Помощь"""
    question = models.TextField(verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')

    class Meta:
        verbose_name = 'Помощь'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question


class Collection(models.Model):
    """Коллекция"""
    image = models.ImageField(verbose_name='Фото')
    title = models.CharField(max_length=55, verbose_name='Название')

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Slider(models.Model):
    """Слайдер"""
    image = models.ImageField(upload_to='slider_image', null=True, verbose_name='Фото')
    field_link = models.CharField(max_length=150, blank=True, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'Some image or link'


class BackCall(models.Model):
    """Обратный звонок"""
    STATUS = [
        ('yes', 'Да'),
        ('no', 'Нет'),
    ]
    name = models.CharField(max_length=155, verbose_name='Имя')
    number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number_of_phone = models.CharField(validators=[number_regex], max_length=14, unique=True, null=False, blank=False,
                                       verbose_name='Номер телефона')
    date_of_call = models.DateTimeField(default=datetime.now, verbose_name=u"добавить время")
    status = models.CharField(choices=STATUS, default='no', max_length=155)

    class Meta:
        verbose_name = 'Обратный звонок'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Product(models.Model):
    """Товар"""
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='product',
                                   verbose_name='Коллекция')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    article = models.CharField(max_length=150, verbose_name='Артикль')
    old_price = models.CharField(max_length=150, verbose_name='Старая цена')
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, verbose_name='Скидка')
    new_price = models.IntegerField(blank=True, null=True, verbose_name='Новая цена')
    description = RichTextField(verbose_name='Описание')
    size = models.CharField(max_length=55, default='42-50', verbose_name='Размер')
    line_of_size = models.CharField(max_length=55, blank=True, null=True, verbose_name='Линейка')
    compound = models.CharField(max_length=155, verbose_name='Состав')
    amount = models.PositiveIntegerField(verbose_name='Кол-во', default=1)
    material = models.CharField(max_length=150, verbose_name='Материал')
    new = models.BooleanField(default=False, blank=True, null=True, verbose_name='Новинка')
    hit = models.BooleanField(default=False, blank=True, null=True, verbose_name='Хит продаж')
    favorite = models.BooleanField(default=False, blank=True, null=True, verbose_name='Избранные')

    def save(self):
        if self.discount != 0:
            price_with_discount = (int(self.old_price) * self.discount) / 100
            self.new_price = int(self.old_price) - price_with_discount
            super(Product, self).save()
        else:
            super(Product, self).save()
        self.line_of_size = ((int(self.size[3:]) - int(self.size[0:2])) // 2) + 1
        super(Product, self).save()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ProductImageColor(models.Model):
    """Фотография и цвет для товара"""
    image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='Фото')
    color = RGBColorField()
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='Товары')

    def __str__(self):
        return f'{self.color},{self.image}'


class Footer(models.Model):
    """Футер(первая вкладка)"""
    logo = models.ImageField(upload_to='footer_header', verbose_name='Логотип')
    imformation = models.TextField(verbose_name='Информация')
    number = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Футер(первая вкладка)'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.number


class SecondFooter(models.Model):
    """Футер(вторая вкладка)"""
    MESSENGER = [
        ('number', 'Номер'),
        ('email', 'Почта'),
        ('instagram', 'Instagram'),
        ('telegram', 'Телеграм'),
        ('whatsapp', 'WhatsApp')
    ]
    messen = models.CharField(choices=MESSENGER, max_length=155, verbose_name='Соцсеть')
    link = models.CharField(max_length=16, blank=True, null=True)

    def save(self):
        if self.messen == 'whatsapp':
            self.link = 'https://wa.me/' + self.link
            super(SecondFooter, self).save()
        else:
            super(SecondFooter, self).save()
        super(SecondFooter, self).save()

    class Meta:
        verbose_name = 'Футер(вторая вкладка)'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.messen


class Number(models.Model):
    """Номера для футера"""
    number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number = models.CharField(validators=[number_regex], max_length=14, unique=True, null=False,
                              blank=False, verbose_name='Номер телефона')
    second_footer = models.ForeignKey(SecondFooter, on_delete=models.CASCADE, related_name='footer')


class User(models.Model):
    """Пользователь"""
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
    date_of_order = models.DateTimeField(default=datetime.now, verbose_name=u"добавить время")
    status_of_order = models.CharField(choices=STATUS, default='new', max_length=155, verbose_name='Статус заказа')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
