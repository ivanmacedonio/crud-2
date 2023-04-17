from django.contrib import admin
from Academica.models import *
# Register your models here.

admin.site.register(Carrera)
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Matricula)

#le da la view desde el admin de django lo que permite poder hacer crud con los modelos
# 

