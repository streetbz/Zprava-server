# Generated by Django 2.0.5 on 2018-06-08 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20180608_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textmessage',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='textmessage',
            name='subscriber',
        ),
    ]