# Generated by Django 4.0 on 2021-12-25 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_rename_full_name_order_first_name_order_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]
