# Generated by Django 4.1.1 on 2022-10-07 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0030_alter_plantas_final_nombre_planta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategoria',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.categoria', verbose_name='categoriaS'),
        ),
    ]