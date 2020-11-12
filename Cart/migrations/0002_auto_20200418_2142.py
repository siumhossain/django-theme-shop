# Generated by Django 3.0.4 on 2020-04-18 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carts',
            name='quantity',
        ),
        migrations.AddField(
            model_name='carts',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]
