# Generated by Django 3.2.8 on 2021-11-18 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_collection_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='description',
            field=models.TextField(default='data'),
            preserve_default=False,
        ),
    ]
