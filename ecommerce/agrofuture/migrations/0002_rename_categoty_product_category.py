# Generated by Django 5.0.6 on 2024-06-19 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agrofuture', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categoty',
            new_name='category',
        ),
    ]
