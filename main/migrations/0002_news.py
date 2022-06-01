# Generated by Django 4.0.4 on 2022-06-01 04:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='news')),
                ('title', models.CharField(max_length=150)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
    ]