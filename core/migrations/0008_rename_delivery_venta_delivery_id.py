# Generated by Django 3.2.4 on 2022-06-05 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20220605_0304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='delivery',
            new_name='delivery_id',
        ),
    ]
