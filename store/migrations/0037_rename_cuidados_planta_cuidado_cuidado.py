# Generated by Django 4.1.1 on 2022-10-10 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0036_planta_cuidado_plantas_final_cuidados'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planta_cuidado',
            old_name='cuidados',
            new_name='cuidado',
        ),
    ]
