# Generated by Django 4.2.6 on 2023-11-01 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_menuitem_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='slug',
        ),
    ]
