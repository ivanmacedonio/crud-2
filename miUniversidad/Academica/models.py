from django.db import models

class Carrera(models.Model):

    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion =models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt= "{0} Duracion {1} años"
        return txt.format(self.nombre, self.duracion)

class Estudiante(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellido = models.CharField(max_length=35)
    nombre = models.CharField(max_length=30)
    fechaNacimiento= models.DateField()
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    def nombreCompleto(self):
        txt = "{0} {1}"
        return txt.format(self.apellido, self.nombre)
    
    def __str__(self):
        txt= "{0} - CARRERA {1}, VIGENCIA {2}"
        if self.vigencia == True:
            estado= 'Vigente'
        else:
            estado = 'Irregular'
        return txt.format(self.nombreCompleto(), self.carrera, estado)

    

    
class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)

    def __str__(self):
        txt= "{0} {1} Docente {2}"
        return txt.format(self.nombre, self.codigo, self.docente) 

class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante,  null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,  null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateField(auto_now_add=True)

    def __str__(self):
        txt= "{0} matriculad{1} curso {2}" #el 1 se remplaza por a/o dependiendo el sexo
        if self.estudiante.sexo == 'F':
            letra = 'a'
        else:
            letra = 'o'
        
        return txt.format(self.estudiante.nombreCompleto(), letra, self.curso)

    '''
    Una vez creados los modelos los debemos registrar en el admin para usarlos en la interfaz de django'''