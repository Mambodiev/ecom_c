# Generated by Django 3.0.6 on 2021-04-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_remove_comment_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='ip',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
