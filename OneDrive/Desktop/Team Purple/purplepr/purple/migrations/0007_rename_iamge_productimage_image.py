# Generated by Django 5.1.1 on 2024-11-20 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purple', '0006_remove_products_product_image_productimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='iamge',
            new_name='image',
        ),
    ]
