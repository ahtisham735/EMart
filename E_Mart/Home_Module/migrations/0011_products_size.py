# Generated by Django 3.1.7 on 2021-04-21 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Module', '0010_remove_products_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='size',
            field=models.CharField(choices=[('s', 'small'), ('L', 'Large'), ('M', 'Medium'), ('Nill', 'Not Applicable')], default=('Nill', 'Not Applicable'), max_length=50),
        ),
    ]