# Generated by Django 5.1.1 on 2024-11-18 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purple', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
    ]
