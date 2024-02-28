# Generated by Django 5.0 on 2024-02-28 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=20)),
                ('idade', models.IntegerField()),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('rg', models.CharField(max_length=9, unique=True)),
                ('email', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=11)),
                ('cep', models.CharField(max_length=8)),
                ('endereco', models.CharField(max_length=100)),
                ('numero', models.IntegerField(max_length=5)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('complemento', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=2)),
                ('cargo', models.CharField(max_length=50)),
            ],
        ),
    ]