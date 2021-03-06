# Generated by Django 2.0.5 on 2018-06-09 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_auto_20180608_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='first_side',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='first_user', to='signup.Users'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='second_side',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_user', to='signup.Users'),
        ),
    ]
