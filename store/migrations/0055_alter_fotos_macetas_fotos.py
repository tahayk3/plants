# Generated by Django 4.1.1 on 2022-10-11 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0054_alter_fotos_macetas_fotos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotos_macetas',
            name='fotos',
            field=models.ImageField(null=True, upload_to='imagenes_macetas/', verbose_name='fotos'),
        ),
    ]