# Generated by Django 3.0.4 on 2020-05-06 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_remove_billing_c_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='c_id',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]