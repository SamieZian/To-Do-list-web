# Generated by Django 3.0.8 on 2020-08-23 13:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('geeks_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='geeksmodel',
            name='date_T',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
