# Generated by Django 3.2.4 on 2022-06-05 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_venta_pago_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='pago_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.medio_pago'),
        ),
    ]