# Generated by Django 3.1.7 on 2021-05-24 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Module', '0004_auto_20210519_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('men', "Men's Fashion"), ('women', "Women's Fashion"), ('WBJ', 'Watches,Bags & Jewelery'), ('electronics', 'Electronic Devices'), ('accessories', 'Electronic Accessories'), ('sports', 'Sports'), ('home', 'Home Appliances')], max_length=255),
        ),
    ]
