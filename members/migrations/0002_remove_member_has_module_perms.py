# Generated by Django 5.0.6 on 2024-06-16 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='has_module_perms',
        ),
    ]
