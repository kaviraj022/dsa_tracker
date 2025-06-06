# Generated by Django 5.2.1 on 2025-05-28 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user')], default='user', max_length=5),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterModelTable(
            name='problem',
            table='problems',
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
        migrations.AlterModelTable(
            name='usernote',
            table='usernotes',
        ),
        migrations.AlterModelTable(
            name='userprogress',
            table='userprogress',
        ),
    ]
