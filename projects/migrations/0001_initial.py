# Generated by Django 4.0.1 on 2022-02-01 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Full name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('subject', models.CharField(max_length=200, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'ordering': ('-added',),
            },
        ),
    ]