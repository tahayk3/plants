# Generated by Django 4.1.1 on 2022-10-06 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_recomendaciones'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuidados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuidados', models.CharField(max_length=150, verbose_name='Cuidados')),
            ],
        ),
    ]
