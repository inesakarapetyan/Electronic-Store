# Generated by Django 5.0.6 on 2024-07-25 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_delete_accesorisse'),
    ]

    operations = [
        migrations.CreateModel(
            name='oroduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='product_images/')),
            ],
        ),
    ]
