# Generated by Django 4.1.1 on 2022-10-05 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_pizza_toppings_topping_toppings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topping',
            name='toppings',
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(related_name='pizzas', to='store.topping'),
        ),
    ]
