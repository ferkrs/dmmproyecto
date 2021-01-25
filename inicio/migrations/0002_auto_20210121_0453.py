# Generated by Django 2.2.9 on 2021-01-21 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignacionpersonagrupo',
            name='puesto',
            field=models.IntegerField(choices=[(0, 'MIEMBRO'), (1, 'PRESIDENTE'), (2, 'VICE-PRESIDENTE'), (3, 'SECRETARIA'), (4, 'TESORERA'), (5, 'VOCAL 1'), (6, 'VOCAL 2')], default=0),
        ),
        migrations.AlterField(
            model_name='persona',
            name='cui',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]