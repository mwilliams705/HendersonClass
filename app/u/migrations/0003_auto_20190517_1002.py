# Generated by Django 2.2.1 on 2019-05-17 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('u', '0002_auto_20190516_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email_confirmed',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]
