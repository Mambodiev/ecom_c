# Generated by Django 3.2 on 2022-07-12 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_hero',
            field=models.BooleanField(default=False),
        ),
    ]
