# Generated by Django 3.0.4 on 2020-05-09 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_auto_20200509_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='Confirmed', max_length=30),
        ),
    ]
