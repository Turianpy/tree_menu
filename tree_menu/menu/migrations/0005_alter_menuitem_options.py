# Generated by Django 4.2.6 on 2023-11-01 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_menuitem_level'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitem',
            options={'ordering': ['menu', 'level', 'name'], 'verbose_name': 'Пункт меню', 'verbose_name_plural': 'Пункты меню'},
        ),
    ]
