# Generated by Django 4.0 on 2021-12-26 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_remove_cart_user_cart_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Canceled'), (1, 'Waiting For Verification'), (2, 'Processsing'), (3, 'On The Way'), (4, 'Delivered')], default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='shop.customer'),
        ),
    ]