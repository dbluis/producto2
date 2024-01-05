# Generated by Django 5.0 on 2024-01-05 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0002_alter_material_cantidad_comprada_gramos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='detallematerial',
            name='cantidad_utilizada_gramos',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='material',
            name='cantidad_comprada_gramos',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
