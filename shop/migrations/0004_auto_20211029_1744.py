# Generated by Django 3.2.8 on 2021-10-29 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20211029_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cover_image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cover_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]