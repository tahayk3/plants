# Generated by Django 4.1.1 on 2022-10-10 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0033_alter_subcategoria_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planta_beneficio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.beneficios')),
                ('plantas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.plantas_final')),
            ],
        ),
        migrations.AddField(
            model_name='plantas_final',
            name='beneficios',
            field=models.ManyToManyField(blank=True, through='store.Planta_beneficio', to='store.beneficios'),
        ),
    ]