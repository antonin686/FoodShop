# Generated by Django 3.2.8 on 2021-10-29 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_category_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='availability',
            field=models.SmallIntegerField(choices=[(0, 'NO'), (1, 'YES')], default=1),
        ),
    ]
