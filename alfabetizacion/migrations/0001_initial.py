# Generated by Django 2.2.9 on 2020-12-22 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inicio', '0003_delete_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='MujeresAlfa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_alfabetizadora', models.CharField(max_length=20)),
                ('ciclo', models.DateField()),
                ('fase', models.IntegerField(choices=[(0, 'INCIAL'), (0, 'PRIMERA DE POST'), (0, 'SEGUNDA DE POST')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('integrantes', models.ManyToManyField(to='inicio.Persona')),
            ],
        ),
    ]
