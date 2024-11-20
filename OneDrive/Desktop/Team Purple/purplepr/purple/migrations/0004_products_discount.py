# Generated by Django 5.1.1 on 2024-11-20 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purple', '0003_products_offerprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Discount Percentage', max_digits=5, null=True),
        ),
    ]
