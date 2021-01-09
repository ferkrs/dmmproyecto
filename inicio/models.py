from django.db import models
from django.urls import reverse


class Persona(models.Model):
    cui = models.CharField(max_length=20,blank= False) 
    SEXO = [ 
        (0,""),(1,"M"),(2,"F"),
    ]
    sexo = models.IntegerField(choices=SEXO, default=0, blank=False)
    primer_nombre = models.CharField(max_length=20, blank=False) 
    segundo_nombre = models.CharField(max_length=20,  blank=False) 
    tercer_nombre = models.CharField(max_length=20,  blank=True) 
    primer_apellido = models.CharField(max_length=20, blank=False) 
    segundo_apellido = models.CharField(max_length=20,  blank=True)
    apellido_casada = models.CharField(max_length=20,  blank=True) 
    fecha_nacimiento = models.DateField(blank=False, null=False)
    telefono= models.CharField(max_length=8, blank=True)
        #quitar direccion
    direccion = models.CharField(max_length=20, blank=True)
    correo_electronico = models.EmailField(max_length=100, blank=True)
    def __str__(self):
        txt="Nombre: {0} {1}, Telefono: {2}"
        return txt.format(self.primer_nombre, self.primer_apellido, self.telefono) 
    def persona_list(self): 
        txt="{0} (Nombre: {1} {2})"
        return txt.format(self.cui, self.primer_nombre, self.primer_apellido)
    class Meta:
        verbose_name = "Registro de personas"
        verbose_name_plural = "Registro de personas"

class Grupo(models.Model):
    nombre_grupo = models.CharField(max_length=50)
    DEPARTAMENTO = [ 
        (0,"SAN MARCOS"),
    ]
    departamento = models.IntegerField(choices=DEPARTAMENTO, default=0, blank=False)
    MUNICIPIO = [ 
        (0,"SAN PEDRO"),
    ]
    municipio = models.IntegerField(choices=MUNICIPIO, default=0, blank=False)

    IDENTIFICADOR = [ 
        (0, "AREA RURAL"), 
        (1, "AREA URBANA"), 
        (2, "LLANO GRANDE")
    ]
    identificador= models.IntegerField(choices=IDENTIFICADOR, blank=False)
    #AREA URBANA
    ZONA= [ 
        (0, ""), (1, "ZONA 1"),(2, "ZONA 1 Y 2"),
        (3, "ZONA 1 Y 4"),(4, "ZONA 2"),
        (5, "ZONA 4"),(6, "ZONA 3 Y 4"),

    ]
    zona = models.IntegerField(choices=ZONA,default=0, blank=True)

    CASERIO= [ 
        (0, ""), (1, "LOS JAZMINES"),(2, "LLANO GRANDE"),
    ]
    caserio = models.IntegerField(choices=CASERIO,default=0, blank=True)

    CANTON= [ 
        (0, ""),(1, "LA PARROQUIA"),(2, "SANTA MARIA DE ATOCHA"),
        (3, "SAN MIGUEL"),(4, "SAN JUAN DE DIOS"),
        (5, "SAN JUAN DEL POZO"),(6, "SAN AGUSTÍN TONALÁ"),
        (7, "EL MOSQUITO"),(8, "SAN SEBASTIÁN"),
    ]
    canton = models.IntegerField(choices=CANTON,default=0, blank=True)
    
    SECTOR= [ 
        (0, ""),(1, "HIERBA BUENA"),(2, "GALLO ROJO"),
    ]
    sector = models.IntegerField(choices=SECTOR,default=0, blank=True)
    #AREA RURAL

    ALDEAS= [ 
        (0, ""),(1, "CANTEL"),(2, "CORRAL GRANDE"),
        (3, "CHAMPOLLAP"),(4, "CHIM"),
        (5, "EL CEDRO"),(6, "EL TABLERO"),
        (7, "LA GRANDEZA"),(8, "MÁVIL"),
        (9, "PIEDRA GRANDE"),(10, "PROVINCIA CHIQUITA"),
        (11, "SACUCHÚM"),(12, "SAN ANDRÉS CHÁPIL"),
        (13, "SAN ISIDRO CHAMAC"),(14, "SAN JOSÉ CÁBEN"),
        (15, "SAN PEDRO PETZ"),(16, "SANTA TERESA"),
        (17, "SAN FRANCISCO SOCHE"),
    ]
    aldeas = models.IntegerField(choices=ALDEAS,default=0, blank=True)
    paraje = models.CharField(max_length=20,blank=True)

    #cambiar el modelo para obtener el id
    def grupo_id(self): 
        return str(self.id)
    class Meta:
        verbose_name = "Asiganacion de grupos"
        verbose_name_plural = "Asiganacion de grupos"

class RelacionDPG(models.Model): 
    DIRECTIVA = [
        (0, "MIEMBRO"), 
        (1, "PRESIDENTE"), 
        (2, "VICE-PRESIDENTE"),
        (3, "SECRETARIA"),
        (4, "TESORERA"), 
        (5, "VOCAL 1"),
        (6, "VOCAL 2"),

    ]
    persona = models.ForeignKey(Persona, on_delete= models.CASCADE,related_name='persona_directiva', null=False, blank=False)
    puesto = models.IntegerField(choices=DIRECTIVA, null=False, blank=False, default=0)
    grupo = models.ForeignKey(Grupo, on_delete= models.CASCADE,related_name='grupo_directiva',null=False, blank=False)
    def __str__(self): 
        return str(self.id)
    #mostrar la relacion entre la persona y el puest
  
    def directiva_grupo(self):
        return "\n".join([p.grupo_id() for p in self.grupo.all()])

    class Meta:
        verbose_name = "Asignar Directiva"
        verbose_name_plural = "Asignar Directiva"
#cambiar de modelo
