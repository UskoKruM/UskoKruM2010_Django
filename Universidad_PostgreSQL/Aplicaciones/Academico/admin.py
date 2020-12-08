from django.contrib import admin
from .models import Curso

# Register your models here.


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    # list_display = ('id', 'nombre', 'creditos')
    # ordering = ('creditos', 'nombre')
    # search_fields = ('nombre', 'creditos')
    # list_editable = ('nombre','creditos')
    # list_display_links = ('nombre',)
    # list_filter = ('creditos',)
    # list_per_page = 3 # Paginación
    exclude = ('creditos',)

    def datos(self, obj):
        return obj.nombre.upper()

    datos.short_description = 'XYA'

# admin.site.register(Curso, CursoAdmin)

# admin.site.register(Curso)
# admin.site.register(Curso, CursoAdmin)
