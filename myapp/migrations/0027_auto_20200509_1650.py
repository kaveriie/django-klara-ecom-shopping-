# Generated by Django 3.0.4 on 2020-05-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_order_expecteddelivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expecteddelivery',
            field=models.DateField(null=True),
        ),
    ]
