# Generated by Django 4.1.1 on 2022-10-10 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0044_macetas_final'),
    ]

    operations = [
        migrations.AlterField(
            model_name='macetas_final',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='macetas_final',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.material', verbose_name='material de maceta'),
        ),
    ]
