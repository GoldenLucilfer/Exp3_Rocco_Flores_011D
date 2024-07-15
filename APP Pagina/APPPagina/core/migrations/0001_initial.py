# Generated by Django 5.0.6 on 2024-06-21 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beat',
            fields=[
                ('idBeat', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id del beat')),
                ('nombreBeat', models.CharField(max_length=50, verbose_name='Nombre del Beat')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion del Beat')),
                ('nombreColab', models.CharField(blank=True, max_length=50, verbose_name='Nombre Colaboracion')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id del Usuario')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=20, verbose_name='Apellido')),
                ('nombreUsuario', models.CharField(max_length=20, verbose_name='Nombre del Usuario')),
                ('email', models.EmailField(max_length=254, verbose_name='Mail de Usuario')),
            ],
        ),
    ]