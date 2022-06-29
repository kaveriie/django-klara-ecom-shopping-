# Generated by Django 3.0.4 on 2020-04-23 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200422_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewdate', models.DateTimeField(auto_now_add=True)),
                ('reviewrating', models.IntegerField(default=0)),
                ('reviewtext', models.CharField(max_length=500)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Customer')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Products')),
            ],
        ),
    ]
