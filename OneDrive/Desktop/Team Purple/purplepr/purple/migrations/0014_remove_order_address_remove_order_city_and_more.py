# Generated by Django 5.1.1 on 2024-11-27 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purple', '0013_order_address_order_city_order_pincode_order_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='order',
            name='state',
        ),
    ]