# Generated by Django 4.1.1 on 2022-10-06 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_rename_id_categoria_subcategoria_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategoria',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.categoria', verbose_name='Categoria'),
        ),
    ]