# Generated by Django 4.1.1 on 2022-10-06 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_subcategoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategoria',
            old_name='id_categoria',
            new_name='categoria',
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='nombre_sub_categoria',
            field=models.CharField(blank=True, max_length=75, verbose_name='nombre_sub_categoria'),
        ),
    ]