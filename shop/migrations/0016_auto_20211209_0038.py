# Generated by Django 3.2.9 on 2021-12-08 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_customer_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cover_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='cover_image',
            new_name='image',
        ),
    ]
