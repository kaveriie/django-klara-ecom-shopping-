# Generated by Django 3.0.4 on 2020-05-04 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_user_productimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='productimage',
            new_name='profilepic',
        ),
    ]
