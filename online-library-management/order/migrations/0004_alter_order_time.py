# Generated by Django 3.2.20 on 2023-12-30 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
