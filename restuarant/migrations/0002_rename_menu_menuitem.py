# Generated by Django 5.0.6 on 2024-06-13 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restuarant', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu',
            new_name='MenuItem',
        ),
    ]