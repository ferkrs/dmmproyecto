from django.db import models
from django.urls import reverse


class Persona(models.Model):
    cui = models.CharField(max_length=20,blank= False) 
    primer_nombre = models.CharField(max_length=20, blank=False) 
    segundo_nombre = models.CharField(max_length=20, null=True, blank=True) 
    tercer_nombre = models.CharField(max_length=20, null=True, blank=True) 
    primer_apellido = models.CharField(max_length=20, blank=False) 
    segundo_apellido = models.CharField(max_length=20, null=True, blank=True)
    apellido_casada = models.CharField(max_length=20, null=True, blank=True) 
    fecha_nacimiento = models.DateField(blank= True, null=True)
    telefono= models.CharField(max_length=8, blank= False)
    direccion = models.CharField(max_length=20,blank= False)
    correo_electronico = models.EmailField(max_length=100)
    def __str__(self): 
        txt="{0} (Nombre: {1} {2})"
        return txt.format(self.cui, self.primer_nombre, self.primer_apellido)
    
    class Meta:
        verbose_name = "Registro de personas"
        verbose_name_plural = "Registro de personas"

class Grupo(models.Model):
    DEPARTAMENTO = [ 
        (0,"SAN MARCOS"),
    ]
    departamento = models.IntegerField(choices=DEPARTAMENTO, default=0)
    MUNICIPIO = [ 
        (0,"SAN PEDRO"),
    ]
    municipio = models.IntegerField(choices=MUNICIPIO, default=0)

    IDENTIFICADOR = [ 
        (0, "AREA RURAL"), 
        (1, "AREA URBANA"), 
        (2, "LLANO GRANDE")
    ]
    identificador= models.IntegerField(choices=IDENTIFICADOR)
    #AREA URBANA
    ZONA= [ 
        (0, "ZONA 1"),(1, "ZONA 1 Y 2"),
        (2, "ZONA 1 Y 4"),(3, "ZONA 2"),
        (4, "ZONA 4"),(5, "ZONA 3 Y 4"),

    ]
    zona = models.IntegerField(choices=ZONA,null=False, blank=False)

    CASERIO= [ 
        (0, "LOS JAZMINES"),(1, "LLANO GRANDE"),
    ]
    caserio = models.IntegerField(choices=CASERIO,null=False, blank=False)

    CANTON= [ 
        (0, "LA PARROQUIA"),(1, "SANTA MARIA DE ATOCHA"),
        (2, "SAN MIGUEL"),(3, "SAN JUAN DE DIOS"),
        (4, "SAN JUAN DEL POZO"),(5, "SAN AGUSTÍN TONALÁ"),
        (6, "EL MOSQUITO"),(7, "SAN SEBASTIÁN"),
    ]
    canton = models.IntegerField(choices=CANTON,null=False, blank=False)
    
    SECTOR= [ 
        (0, "HIERBA BUENA"),(1, "GALLO ROJO"),
    ]
    sector = models.IntegerField(choices=SECTOR,null=False, blank=False)
    #AREA RURAL

    ALDEAS= [ 
        (0, "CANTEL"),(1, "CORRAL GRANDE"),
        (2, "CHAMPOLLAP"),(3, "CHIM"),
        (4, "EL CEDRO"),(5, "EL TABLERO"),
        (6, "LA GRANDEZA"),(7, "MÁVIL"),
        (8, "PIEDRA GRANDE"),(9, "PROVINCIA CHIQUITA"),
        (10, "SACUCHÚM"),(11, "SAN ANDRÉS CHÁPIL"),
        (12, "SAN ISIDRO CHAMAC"),(13, "SAN JOSÉ CÁBEN"),
        (14, "SAN PEDRO PETZ"),(15, "SANTA TERESA"),
        (16, "SAN FRANCISCO SOCHE"),
    ]
    aldeas = models.IntegerField(choices=ALDEAS,null=False, blank=False)
    paraje = models.CharField(max_length=20, null=True, blank=True)
    nombre_grupo = models.CharField(max_length=20,blank= False)
    integrantes = models.ManyToManyField(Persona)
    def __str__(self): 
        txt="{0}"
        return txt.format(self.nombre_grupo)
    class Meta:
        verbose_name = "Asiganacion de grupos"
        verbose_name_plural = "Asiganacion de grupos"

class RelacionDPG(models.Model): 
    DIRECTIVA = [
        (0, "PRESIDENTE"), 
        (1, "VICE-PRESIDENTE"), 
        (2, "SECRETARIA"),
        (3, "TESORERA"), 
        (4, "VOCAL 1"),
        (5, "VOCAL 2"),  
    ]
    persona = models.ForeignKey(Persona, on_delete= models.CASCADE,related_name='persona_directiva', null=False, blank=False)
    puesto = models.IntegerField(choices=DIRECTIVA, null=False, blank=False)
    grupo = models.ForeignKey(Grupo, on_delete= models.CASCADE,related_name='grupo_directiva',null=False, blank=False)
    def __str__(self): 
        txt="{0} (Hola: {1})"
        return txt.format(self.puesto)

    class Meta:
        verbose_name = "Asignar Directiva"
        verbose_name_plural = "Asignar Directiva"

class Curso(models.Model):
    MODALIDAD = [
        (0, "CURSO"), 
        (1, "TALLER"), 
        (2, "SEMINARIO"),
        (3, "DIPLOMADO"), 
        (4, "CAPACITACION"),
        (5, "CONVERSATORIO"),  
    ] 
    modalidad = models.IntegerField(choices=MODALIDAD, null=False, blank=False)
    nombre = models.CharField(max_length=20, blank=False) 
    fecha_inicio = models.DateField(blank= True, null=True)
    fecha_finalizacion = models.DateField(blank= True, null=True)
    hora_inicio = models.TimeField(auto_now=False)
    hora_final = models.TimeField(auto_now=False)
    DIAS = [
        (0, "LUNES"), 
        (1, "MARTES"), 
        (2, "MIERCOLES"),
        (3, "JUEVES"), 
        (4, "VIERNES"),
        (5, "SABADO"),  
        (6, "DOMINGO") 
    ]
    de = models.IntegerField(choices=DIAS, null=False, blank=False)
    a = models.IntegerField(choices=DIAS, null=False, blank=False)
    integrantes = models.ManyToManyField(Persona)
    #falta agregar a los responsables
    