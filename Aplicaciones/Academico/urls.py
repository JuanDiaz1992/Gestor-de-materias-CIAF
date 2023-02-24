from django.urls import path
from django.contrib.auth.decorators import login_required
from Aplicaciones.Academico.views import eliminar_curso, creado,CursoListView,modificarPerfilEst,cambiarFotoPerfil
from Aplicaciones.Academico.views import modificar_curso,editarCurso,registrar_curso
from . import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('',login_required(CursoListView.as_view()), name= 'gestion__cursos'),    
    #path('',login_required(EstCurso), name= 'gestion__cursos'),
    path('eliminacionCurso/<int:id>', eliminar_curso),
    path('edicionCurso/<int:id>', login_required (modificar_curso)),
    path('editarCurso/',login_required (editarCurso)),
    path('registraCurso/',login_required(registrar_curso), name='agregarCurso'),
    path('register/', views.register, name = 'register'),
    path('modPerfEst/', views.modificarPerfilEst, name = 'ModificarPerfil'),
    path('modFotoPerfil/', views.cambiarFotoPerfil, name = 'cambiarPerfil'),
    path('creado/', creado, name = 'creado'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)