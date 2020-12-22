# Generated by Django 2.2.9 on 2020-12-22 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alfabetizacion', '0002_mujeresalfa_comunidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comunidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comunidad', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='mujeresalfa',
            options={'verbose_name': 'Grupos de alfabetizacion', 'verbose_name_plural': 'Grupos de alfabetizacion'},
        ),
        migrations.AlterField(
            model_name='mujeresalfa',
            name='comunidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alfabetizacion.Comunidad', verbose_name='comunidades'),
        ),
        migrations.AlterField(
            model_name='mujeresalfa',
            name='fase',
            field=models.IntegerField(choices=[(0, 'FASE INCIAL'), (1, 'PRIMERA DE POST'), (2, 'SEGUNDA DE POST')]),
        ),
    ]
