# Generated by Django 4.0.4 on 2022-06-16 17:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_remove_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='number_of_phone',
            field=models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Номер телефона'),
        ),
    ]
