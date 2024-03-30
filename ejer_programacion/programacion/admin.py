from django.contrib import admin

from .models import Conductor,Sede, Propietario,Encomienda,Vehiculo,Programacion

# Register your models here.


from import_export.admin import ImportExportModelAdmin

admin.site.register(Propietario)
admin.site.register(Conductor)

admin.site.register(Sede)
admin.site.register(Vehiculo)



@admin.register(Programacion)
class ProgramacionAdmin(ImportExportModelAdmin):
    list_display = ('codigo', 'vehiculo','conductor','origen','destino','programacion','precio','estado', 'fecha_creado', "fecha_actualizado",)
    list_filter = ['codigo', 'vehiculo','conductor','origen','destino','programacion','precio','estado', 'fecha_creado', "fecha_actualizado",]
    search_fields = ['codigo']



admin.site.register(Encomienda) 