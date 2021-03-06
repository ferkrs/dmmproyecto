# Generated by Django 2.2.9 on 2021-02-17 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_auto_20210217_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='aldeas',
            field=models.IntegerField(blank=True, choices=[(1, 'CANTEL'), (2, 'CORRAL GRANDE'), (3, 'CHAMPOLLAP'), (4, 'CHIM'), (5, 'EL CEDRO'), (6, 'EL TABLERO'), (7, 'LA GRANDEZA'), (8, 'MÁVIL'), (9, 'PIEDRA GRANDE'), (10, 'PROVINCIA CHIQUITA'), (11, 'SACUCHÚM'), (12, 'SAN ANDRÉS CHÁPIL'), (13, 'SAN ISIDRO CHAMAC'), (14, 'SAN JOSÉ CÁBEN'), (15, 'SAN PEDRO PETZ'), (16, 'SANTA TERESA'), (17, 'SAN FRANCISCO SOCHE')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='canton',
            field=models.IntegerField(blank=True, choices=[(1, 'LA PARROQUIA'), (2, 'SANTA MARIA DE ATOCHA'), (3, 'SAN MIGUEL'), (4, 'SAN JUAN DE DIOS'), (5, 'SAN JUAN DEL POZO'), (6, 'SAN AGUSTÍN TONALÁ'), (7, 'EL MOSQUITO'), (8, 'SAN SEBASTIÁN')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='caserio',
            field=models.IntegerField(blank=True, choices=[(1, 'Agua Tibia'), (2, 'Alta Vista'), (3, 'Bella Vista'), (4, 'Ciprés Grande'), (5, 'Cruz de Piedra'), (6, 'Cruz Verde'), (7, 'El Boquerón'), (8, 'El Platanillo'), (9, 'El Tizate'), (10, 'Entre Ríos'), (11, 'Ixcá'), (12, 'Ixhual '), (13, 'Ixhual 2 '), (14, 'La Cuchilla'), (15, 'La Democracia'), (16, 'La Lagunac '), (17, 'La Libertad '), (18, 'Las Guayabas'), (19, 'Las Vásquez'), (20, 'Loma Linda'), (21, 'Los Juárez'), (22, 'Los Molinos'), (23, 'Nueva Reforma'), (24, 'Ojo de Agua'), (25, 'Oratorio'), (26, 'Paconché'), (27, 'Palencia '), (28, 'Piedra Parada'), (29, 'San Francisco El Chichicaste'), (30, 'San Juan del Pozo'), (31, 'San Miguel Las Flores'), (32, 'San Rafael'), (33, 'San Vicente Esquipulas'), (34, 'Santa Teresa')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='direccion_alternativa',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='paraje',
            field=models.IntegerField(blank=True, choices=[(1, 'Canichel'), (2, 'Joya del Porvenir'), (3, 'El Plan'), (4, 'Ajil'), (5, 'Buena Vista'), (6, 'San Francisco'), (7, 'Agua Caliente'), (8, 'El Zapote'), (9, 'La Industria'), (10, 'El Tesoro'), (11, 'Las Flores'), (12, 'Vista Hermosa'), (13, 'La Libertad'), (14, 'Los Bravo'), (15, 'La Ciénaga'), (16, 'Alta Vista'), (17, 'San Rafael'), (18, 'La Comunidad l'), (19, 'Carolina'), (20, 'Kusinché'), (21, 'Santa Rita I'), (22, 'Santa Rita II'), (23, 'Los Coyotes'), (24, 'Agua Bendita'), (25, 'La Michada'), (26, 'La Providencia'), (27, 'López'), (28, 'El Zarco'), (29, 'Villa El Progreso'), (30, 'El Carmen'), (31, 'Esquipulas'), (32, 'Ixcá'), (33, 'Las Escobas'), (34, 'San Lorenzo'), (35, 'San Miguel'), (36, 'San Martín'), (37, 'San Pedrito'), (38, 'La Caballería'), (39, 'Ojo de Agua'), (40, 'Villa Nueva'), (41, 'Cerro Grande'), (42, 'Las Piedrecitas'), (43, 'Paraje Agua Tibia'), (44, 'Sector Monterrey'), (45, 'Sector Tres Fuentes'), (46, 'Sector Los Ramírez'), (47, 'Sector Fraternidad')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='sector',
            field=models.IntegerField(blank=True, choices=[(1, 'HIERBA BUENA'), (2, 'GALLO ROJO'), (2, 'LOS JAZMINES'), (3, 'LLANO GRANDE')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='zona',
            field=models.IntegerField(blank=True, choices=[(1, 'ZONA 1'), (2, 'ZONA 1 Y 2'), (3, 'ZONA 1 Y 4'), (4, 'ZONA 2'), (5, 'ZONA 4'), (6, 'ZONA 3 Y 4')], default=0, null=True),
        ),
    ]
