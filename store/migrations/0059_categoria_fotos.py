# Generated by Django 4.1.1 on 2022-10-11 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0058_remove_habilidadempleado_empleado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='fotos',
            field=models.ImageField(null=True, upload_to='imagenes_categorias/', verbose_name='Foto'),
        ),
    ]