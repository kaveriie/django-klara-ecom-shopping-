# Generated by Django 3.0.4 on 2020-05-09 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='expecteddelivery',
            field=models.DateTimeField(null=True),
        ),
    ]