# Generated by Django 5.0 on 2024-03-05 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=150),
        ),
    ]
