# Generated by Django 5.0 on 2023-12-29 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='cantidad_comprada_gramos',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
