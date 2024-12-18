# Generated by Django 5.1.1 on 2024-11-25 06:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purple', '0009_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('COD', 'Cash on Delivery'), ('Online', 'Online Payment')], max_length=100)),
                ('product_ids', models.CharField(max_length=255, null=True)),
                ('product_names', models.CharField(max_length=255, null=True)),
                ('total_price', models.FloatField(default=0.0)),
                ('status', models.CharField(choices=[('WAITING FOR CONFIRMATION', 'Waiting for confirmation'), ('CONFIRMED', 'Confirmed'), ('OUT FOR DELIVERY', 'Out for delivery'), ('DELIVERED', 'Delivered'), ('REJECTED', 'Rejected')], default='WAITING FOR CONFIRMATION', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order_ids', models.CharField(blank=True, max_length=100, null=True)),
                ('total_cart_items', models.PositiveIntegerField(default=0)),
                ('selected_weights', models.TextField(blank=True, null=True)),
                ('quantities', models.TextField(blank=True, null=True)),
                ('delivery_pin', models.CharField(blank=True, max_length=6, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
