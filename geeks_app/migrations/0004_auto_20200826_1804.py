# Generated by Django 3.0.8 on 2020-08-26 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks_app', '0003_geeklogin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geeklogin',
            name='userPassword',
            field=models.CharField(max_length=30),
        ),
    ]
