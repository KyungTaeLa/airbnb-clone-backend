# Generated by Django 5.0.6 on 2024-06-11 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='citry',
            new_name='city',
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
