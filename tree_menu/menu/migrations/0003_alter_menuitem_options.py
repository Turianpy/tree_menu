# Generated by Django 4.2.6 on 2023-10-31 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_remove_menu_url_menu_named_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitem',
            options={'ordering': ['menu', 'order', 'name'], 'verbose_name': 'Пункт меню', 'verbose_name_plural': 'Пункты меню'},
        ),
    ]