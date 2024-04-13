from django.contrib import admin
from django.contrib.admin.options import get_content_type_for_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry, ADDITION


from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Conductor,Sede, Propietario,Encomienda,Vehiculo,Programacion,Class


### link del que tome el ejemplo https://ranvir.xyz/blog/django-admin-tips-and-tricks/#handling-history-model-logs-in-django-admin-panel

# Register your models here.


from import_export.admin import ImportExportModelAdmin

admin.site.site_header = 'TITULO'
admin.site.index_title = 'Aplicativo'



###clase con la que queria sacar ultimo usuario

@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change:
            change_message = '{} - {} - {}- {}'.format(obj.sede, obj.tipo, obj.fecha_creado, obj.fecha_actualizado)
            LogEntry.objects.create(
                user=request.user,
                content_type=get_content_type_for_model(obj),
                object_id=obj.id,
                action_flag=2,
                change_message=change_message,
                object_repr=obj.__str__()[:200]
            )
def link_function(field_name):
    def return_function(obj):
        obj_attr = getattr(obj, field_name)
        model = type(obj_attr)
        print(field_name, obj_attr, model)
        return mark_safe('<a href="{}">{}</a>'.format(reverse(
            'admin:{}_{}_change'.format(
                model._meta.app_label,
                model.__name__.lower()
            ), args=(obj_attr.id,)), obj_attr))

    return_function.short_description = field_name
    return return_function

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    readonly_fields = ('sede',)

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        # get all the fields
        all_fields = model._meta.get_fields()
        for field in all_fields:
            # Check if the field is a Foreign Key
            if not (isinstance(field, models.ForeignKey)):
                continue

            # We have to set a new field whose value is a function.
            # The function should return inners of a HTML anchor tag.
            setattr(self, 'main_new', link_function(field.name))
            self.readonly_fields += ('main_new',)
    



admin.site.register(Propietario)
admin.site.register(Conductor)
admin.site.register(Vehiculo)



@admin.register(Programacion)
class ProgramacionAdmin(ImportExportModelAdmin):
    list_display = ('codigo', 'vehiculo','conductor','origen','destino','programacion','precio','estado', 'fecha_creado', "fecha_actualizado",)
    list_filter = ['codigo', 'vehiculo','conductor','origen','destino','programacion','precio','estado', 'fecha_creado', "fecha_actualizado",]
    search_fields = ['codigo']



admin.site.register(Encomienda) 