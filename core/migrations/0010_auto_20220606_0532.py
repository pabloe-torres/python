# Generated by Django 3.2.4 on 2022-06-06 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_delivery_cliente_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='carrito_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.carrito'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='vendedor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.vendedor'),
        ),
    ]
