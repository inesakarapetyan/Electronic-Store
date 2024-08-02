# Generated by Django 5.0.6 on 2024-07-03 11:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_product_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictures', models.ImageField(upload_to='product_images/')),
                ('size', models.PositiveIntegerField(verbose_name='Product size (GB)')),
                ('description', models.TextField(verbose_name='Product description')),
                ('in_stock', models.BooleanField(default=True)),
                ('color', models.CharField(max_length=25, verbose_name='Product color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
    ]
