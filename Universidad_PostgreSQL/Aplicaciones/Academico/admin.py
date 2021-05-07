from django.contrib import admin
from .models import Curso, Docente

# Register your models here.


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'coloreado', 'creditos')
    # ordering = ('creditos', 'nombre')
    # search_fields = ('nombre', 'creditos')
    # list_editable = ('nombre','creditos')
    # list_display_links = ('nombre',)
    # list_filter = ('creditos',)
    # list_per_page = 3 # Paginación
    # exclude = ('creditos',)

    """
    fieldsets = (
        (None, {
            'fields': ('nombre',)
        }),
        ('Advanced options', {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': ('creditos',)
        })
    )
    """

    def datos(self, obj):
        return obj.nombre.upper()

    datos.short_description = "CURSO (MAYÚS)"
    datos.empty_value_display = "???"
    datos.admin_order_field = 'nombre'


# admin.site.register(Curso)
# admin.site.register(Curso, CursoAdmin)

admin.site.register(Docente)
