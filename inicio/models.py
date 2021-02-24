from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# USUARIO
class Usuario(AbstractUser):
    # Este modelo permite almacenar la información de los usuarios para ingresar al sistema

    # Rol
    ROLES = [
        (0, "Administrador"),
        (1, "Trabajador Social"),
        (2, "Tecnico Capacitador"),
        (3, "Promotor de grupos sociales"),
        (5, "Secretaria")
    ]
    rol = models.PositiveSmallIntegerField(choices=ROLES)

    # Campos requeridos
    REQUIRED_FIELDS = ['password','first_name', 'last_name', 'rol', 'email']

# PERSONA
class Persona(models.Model):
    # CUI
    cui = models.CharField(max_length=20,blank= False, unique="true")
    # Sexo
    SEXO = [
        (0,""),(1,"M"),(2,"F"),
    ]
    sexo = models.IntegerField(choices=SEXO, default=0, blank=False)
    # Primer nombre
    primer_nombre = models.CharField(max_length=20, blank=False)
    # Segundo nombre
    segundo_nombre = models.CharField(max_length=20,  blank=True)
    # Tercer nombre
    tercer_nombre = models.CharField(max_length=20,  blank=True)
    # Primer apellido
    primer_apellido = models.CharField(max_length=20, blank=False)
    # Segundo apellido
    segundo_apellido = models.CharField(max_length=20,  blank=True)
    # Apellido casada
    apellido_casada = models.CharField(max_length=20,  blank=True)
    # Fecha Nacimiento
    fecha_nacimiento = models.DateField(blank=False, null=False)
    # Telefono
    telefono= models.CharField(max_length=8, blank=True,null=False)
        #quitar direccion
    direccion = models.CharField(max_length=50, blank=True, null=True)
    # Correo electronico
    correo_electronico = models.EmailField(max_length=100, blank=True, null=False)
    def __str__(self):
        txt="{0} {1} {2} {3} {4}"
        return txt.format(self.cui, self.primer_nombre, self.segundo_nombre, self.primer_apellido, self.segundo_apellido)
    def nombre_completo(self):
        txt="{0} {1} {2} {3}"
        return txt.format(self.primer_nombre, self.segundo_nombre, self.primer_apellido, self.segundo_apellido)
    def telefono_persona(self):
        txt="{0}"
        return txt.format(self.telefono)
    def correo_persona(self):
        txt="{0}"
        return txt.format(self.   correo_electronico)

class Grupo(models.Model):
    # Departamentos
    DEPARTAMENTO = [
        (0,"SAN MARCOS"),
    ]
    departamento = models.IntegerField(choices=DEPARTAMENTO, default=0, blank=False)
    # Municipios
    MUNICIPIO = [
        (0,"SAN PEDRO"),
    ]
    municipio = models.IntegerField(choices=MUNICIPIO, default=0, blank=False)

    # Area
    IDENTIFICADOR = [
        (1, "AREA RURAL"),
        (2, "AREA URBANA"),
        (3, "LLANO GRANDE")
    ]
    identificador= models.IntegerField(choices=IDENTIFICADOR, blank=False)
    # Zonas area urbana
    ZONA= [
        (1, "ZONA 1"),(2, "ZONA 1 Y 2"),
        (3, "ZONA 1 Y 4"),(4, "ZONA 2"),
        (5, "ZONA 4"),(6, "ZONA 3 Y 4"),

    ]
    zona = models.IntegerField(choices=ZONA,default=0, blank=True, null=True)
    # Caserio
    CASERIO= [
        (1, "Agua Tibia"),(2, "Alta Vista"),
        (3, "Bella Vista"),(4, "Ciprés Grande"),
        (5, "Cruz de Piedra"),(6, "Cruz Verde"),
        (7, "El Boquerón"),(8, "El Platanillo"),
        (9, "El Tizate"),(10, "Entre Ríos"),
        (11, "Ixcá"),(12, "Ixhual "),
        (13, "Ixhual 2 "),(14, "La Cuchilla"),
        (15, "La Democracia"),(16, "La Lagunac "),
        (17, "La Libertad "),(18, "Las Guayabas"),
        (19, "Las Vásquez"),(20, "Loma Linda"),
        (21, "Los Juárez"),(22, "Los Molinos"),
        (23, "Nueva Reforma"),(24, "Ojo de Agua"),
        (25, "Oratorio"),(26, "Paconché"),
        (27, "Palencia "),(28, "Piedra Parada"),
        (29, "San Francisco El Chichicaste"),(30, "San Juan del Pozo"),
        (31, "San Miguel Las Flores"),(32, "San Rafael"),
        (33, "San Vicente Esquipulas"),(34, "Santa Teresa"),


    ]
    caserio = models.IntegerField(choices=CASERIO,default=0, blank=True, null=True)
    # Canton
    CANTON= [
        (1, "LA PARROQUIA"),(2, "SANTA MARIA DE ATOCHA"),
        (3, "SAN MIGUEL"),(4, "SAN JUAN DE DIOS"),
        (5, "SAN JUAN DEL POZO"),(6, "SAN AGUSTÍN TONALÁ"),
        (7, "EL MOSQUITO"),(8, "SAN SEBASTIÁN"),
    ]
    canton = models.IntegerField(choices=CANTON,default=0, blank=True,null=True)
    # Sector y caserios se iran juntos
    SECTOR= [
        (1, "HIERBA BUENA"),(2, "GALLO ROJO"),
        (2, "LOS JAZMINES"),(3, "LLANO GRANDE"),
    ]
    sector = models.IntegerField(choices=SECTOR,default=0, blank=True,null=True)

    #AREA RURAL
    ALDEAS= [
        (1, "CANTEL"),(2, "CORRAL GRANDE"),
        (3, "CHAMPOLLAP"),(4, "CHIM"),
        (5, "EL CEDRO"),(6, "EL TABLERO"),
        (7, "LA GRANDEZA"),(8, "MÁVIL"),
        (9, "PIEDRA GRANDE"),(10, "PROVINCIA CHIQUITA"),
        (11, "SACUCHÚM"),(12, "SAN ANDRÉS CHÁPIL"),
        (13, "SAN ISIDRO CHAMAC"),(14, "SAN JOSÉ CÁBEN"),
        (15, "SAN PEDRO PETZ"),(16, "SANTA TERESA"),
        (17, "SAN FRANCISCO SOCHE"),
    ]
    aldeas = models.IntegerField(choices=ALDEAS,default=0, blank=True,null=True)
    PARAJE= [
        (1, "Canichel"),(2, "Joya del Porvenir"),
        (3, "El Plan"),(4, "Ajil"),
        (5, "Buena Vista"),(6, "San Francisco"),
        (7, "Agua Caliente"),(8, "El Zapote"),
        (9, "La Industria"),(10, "El Tesoro"),
        (11, "Las Flores"),(12, "Vista Hermosa"),
        (13, "La Libertad"),(14, "Los Bravo"),
        (15, "La Ciénaga"),(16, "Alta Vista"),
        (17, "San Rafael"),(18, "La Comunidad l"),
        (19, "Carolina"),(20, "Kusinché"),
        (21, "Santa Rita I"),(22, "Santa Rita II"),
        (23, "Los Coyotes"),(24, "Agua Bendita"),
        (25, "La Michada"),(26, "La Providencia"),
        (27, "López"),(28, "El Zarco"),
        (29, "Villa El Progreso"),(30, "El Carmen"),
        (31, "Esquipulas"),(32, "Ixcá"),
        (33, "Las Escobas"),(34, "San Lorenzo"),
        (35, "San Miguel"),(36, "San Martín"),
        (37, "San Pedrito"),(38, "La Caballería"),
        (39, "Ojo de Agua"),(40, "Villa Nueva"),
        (41, "Cerro Grande"),(42, "Las Piedrecitas"),
        (43, "Paraje Agua Tibia"),(44, "Sector Monterrey"),
        (45, "Sector Tres Fuentes"),(46, "Sector Los Ramírez"),
        (47, "Sector Fraternidad"),
    ]
    paraje = models.IntegerField(choices=PARAJE,default=0, blank=True,null=True)
    # Grupo
    direccion_alternativa =models.CharField(max_length=50,blank=True,null=True)
    nombre_grupo = models.CharField(max_length=50)

    def __str__(self):
        txt="{0}"
        return txt.format(self.nombre_grupo)
    class Meta:
        verbose_name = "Asiganacion de grupos"
        verbose_name_plural = "Asiganacion de grupos"


class AsignacionPersonaGrupo(models.Model):
    # Puestos en directiva
    DIRECTIVA = [
        (0, "MIEMBRO"),
        (1, "PRESIDENTE"),
        (2, "VICE-PRESIDENTE"),
        (3, "SECRETARIA"),
        (4, "TESORERA"),
        (5, "VOCAL 1"),
        (6, "VOCAL 2"),
        (7, "VOCAL 3"),
        (8, "VOCAL 4"),
    ]
    # Integrante
    persona = models.ForeignKey(Persona, on_delete= models.CASCADE,related_name='persona_directiva', null=False, blank=False)
    # Puesto a ocupar
    puesto = models.IntegerField(choices=DIRECTIVA, null=False, blank=False, default=0)
    # Grupo al que pertenece
    grupo = models.ForeignKey(Grupo, on_delete= models.CASCADE,related_name='grupo_directiva',null=False, blank=False)
    def full_name(self):
        txt ="{0}"
        return txt.format(self.persona.nombre_completo())
    def persona_puesto(self):
        txt="({0} Puesto: {1} )"
        return txt.format(self.persona, self.puesto)
    def tel_persona(self):
        txt="{0}"
        return txt.format(self.persona.telefono_persona())
    def correo_persona(self):
        txt="{0}"
        return txt.format(self.persona.correo_persona())

