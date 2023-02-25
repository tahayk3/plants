# Generated by Django 4.1.1 on 2022-10-06 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_group_person_membership_group_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=60, verbose_name='apellidos')),
                ('full_name', models.CharField(blank=True, max_length=120, verbose_name='Nombres completos')),
                ('job', models.CharField(choices=[('0', 'CONTADOR'), ('2', 'ADMINISTRADOR'), ('3', 'ECONOMISTA'), ('3', 'OTRO')], max_length=1, verbose_name='Trabajo')),
            ],
            options={
                'verbose_name': 'Mi empleado',
                'verbose_name_plural': 'Empleados de la empresa',
                'ordering': ['-first_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.DeleteModel(
            name='Topping',
        ),
        migrations.AddField(
            model_name='empleado',
            name='Habilidades',
            field=models.ManyToManyField(blank=True, to='store.habilidades'),
        ),
    ]
