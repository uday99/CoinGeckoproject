# Generated by Django 3.0.7 on 2021-03-06 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('username', models.CharField(max_length=150, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('confirmpass', models.CharField(max_length=150)),
            ],
        ),
    ]