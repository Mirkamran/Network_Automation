# Generated by Django 3.2.3 on 2021-06-08 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='price',
            new_name='IP',
        ),
        migrations.RemoveField(
            model_name='item',
            name='image_url',
        ),
    ]
