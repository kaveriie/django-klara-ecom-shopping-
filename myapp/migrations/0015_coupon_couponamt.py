# Generated by Django 3.0.4 on 2020-05-06 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='couponamt',
            field=models.IntegerField(default=1),
        ),
    ]
