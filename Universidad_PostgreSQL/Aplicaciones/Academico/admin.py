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

    # admin.site.register(Curso)
    # admin.site.register(Curso, CursoAdmin)
