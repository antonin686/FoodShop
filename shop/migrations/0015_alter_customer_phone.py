# Generated by Django 3.2.9 on 2021-12-08 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default=2324, max_length=16),
            preserve_default=False,
        ),
    ]
