from django.contrib import admin
from .models import Curso, Docente
from usuario.models import Estudiante

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'creditos')
    ordering = ('-nombre',)
    search_fields = ('nombre','creditos')
    list_display_links = ('nombre',)
    list_filter = ('creditos',)
    list_per_page = 3



admin.site.register(Docente)
admin.site.register(Estudiante)
