# Generated by Django 3.0.7 on 2021-03-07 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_cryptomodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptomodel',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='cryptomodel',
            name='symbol',
            field=models.CharField(max_length=10),
        ),
    ]
