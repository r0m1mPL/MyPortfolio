# Generated by Django 3.2.9 on 2021-11-24 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20211124_2251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectimages',
            options={'verbose_name': 'Картинка к проекту', 'verbose_name_plural': 'Картинки к проекту'},
        ),
    ]