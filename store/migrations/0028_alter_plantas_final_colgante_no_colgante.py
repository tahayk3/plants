# Generated by Django 4.1.1 on 2022-10-07 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_alter_categoria_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantas_final',
            name='colgante_no_colgante',
            field=models.CharField(choices=[('0', 'COLAGANTE'), ('1', 'NO COLGANTE')], max_length=1, verbose_name='Colgante o no colgante'),
        ),
    ]
