# Generated by Django 4.1.1 on 2022-10-06 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_empleado_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='group',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='person',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]