# Generated by Django 4.1.1 on 2022-10-11 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0050_maceta_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maceta_foto',
            old_name='plantas',
            new_name='macetas',
        ),
    ]
