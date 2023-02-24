from django.shortcuts import render, redirect
from .models import Curso
from usuario.models import Estudiante
from django.views.generic import ListView
from .forms import UserRegisterForm, editarDatos, formFotoPerfil, agregarMateria

from django.contrib import messages

from django.contrib.auth import get_user_model
User = get_user_model()



class CursoListView(ListView):
    model = Curso
    template_name = 'gestionCursos.html'
    paginate_by = 6
    def get_queryset(self):
        request = self.request
        user = request.user.id
        id_usuario = User.objects.get(id = user)
        est = Estudiante.objects.get(user_id = id_usuario)
        curl = est.materias.all().order_by('nombre')
        return curl
    def get_context_data(self, **kwargs):
        context = super().get_context_data (**kwargs)
        context ['titulo'] = 'Gestion de Cursos'
        return context
    


def registrar_curso (request):
    user = request.user.id
    id_usuario = User.objects.get(id = user)
    est = Estudiante.objects.get(user_id = id_usuario)
    sem = est.semestre
    if request.method == 'POST':
        form = agregarMateria(request.POST, instance= est)
        if form.is_valid():             
            nombre = request.POST['nombre']
            creditos = request.POST['creditos']
            

            try:
                cur = est.materias.get(nombre = nombre)
                print ("Registro ya existe")
                messages.warning(request, "Esta materia ya se encuetra registrada, ingrese una diferente")

            except:
                curso = Curso.objects.create(nombre=nombre, creditos=creditos, Estudiante = est, semestre = sem)
                return redirect ('/')

    else:
        form=agregarMateria(instance=est)
        
    context={
            'form':form,
        }
    return render (request, "agregarMateria.html", context)



def register (request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        success = False
        if form.is_valid():
            datos = form.save(commit=False)
            datos.save()
            user = form.cleaned_data['username']
            user = User.objects.get(username = user)
            userID = user.id
            primerNombre = form.cleaned_data['nombre1']
            est = Estudiante.objects.get(user_id = userID )
            est.nombre1 = primerNombre
            est.save()

            usename = form.cleaned_data ['username']
            success = True
            messages.add_message(request, messages.INFO, f'Usuario {usename} Registrado Correctamente')
            return render(request, 'creado.html', {'form': form})
        else:
            messages.success(request, f' Datos incorrectos, vuelve a intentarlo')
            return render(request, 'creado.html', {'form': form})

    else:
        form = UserRegisterForm()
    context = {'form':form}
    return render (request, "registrer.html", context)



def modificarPerfilEst(request):
    user = request.user.id
    est = Estudiante.objects.get(user_id = user)  

    if request.method == 'POST':
        form = editarDatos(request.POST, request.FILES, instance= est)
        if form.is_valid():            
            nom1 = request.POST.get('nombre1')            
            nom2 = request.POST.get('nombre2')            
            apel1 = request.POST.get('primerApellido')            
            apel2 = request.POST.get('segundoApellido')
            est.nombre1 = nom1
            est.nombre2 = nom2
            est.segundoApellido = apel2
            est.primerApellido = apel1
            est.save()
            return redirect ('/')
    else:
        form=editarDatos(instance=est)
    context={
            'form':form,
        }
    return render (request, "edicionPerfilEst.html", context)






def cambiarFotoPerfil(request):
    user = request.user.id
    est = Estudiante.objects.get(user_id = user) 
    if request.method == 'POST':
        form = formFotoPerfil(request.POST, request.FILES, instance= est)
        if form.is_valid():            
            fotograp = request.FILES.get('foto')  
            est.foto = fotograp
            est.save()
            return redirect ('/')
    else:
        form=formFotoPerfil(instance=est)
    context={
            'form':form,
        }
    return render (request, "edicionFotoPerfil.html", context)




def  creado ( request ):
    return render(request, "hola.html")


def eliminar_curso(request,id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('/')

def modificar_curso (request,id):
    curso = Curso.objects.get(id=id)
    data = {
        'titulo': 'Edicion de Cursos',
        'curso': curso
    }
    return render(request, "edicionCurso.html", data)

def editarCurso(request):
    id = request.POST['txtId']
    nombre = request.POST['txtNombre']
    creditos = request.POST['txtCreditos']
    curso = Curso.objects.get(id=id)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    return redirect ('/')



"""
def registrar_curso (request):
    user = request.user.id
    id_usuario = User.objects.get(id = user)
    est = Estudiante.objects.get(user_id = id_usuario)
    nombre = request.POST['txtNombre']
    creditos = request.POST['txtCreditos']
    curso = Curso.objects.create(nombre=nombre, creditos=creditos, Estudiante = est)
    return redirect ('/')


def registrar_curso (request):
    user = request.user.id
    id_usuario = User.objects.get(id = user)
    est = Estudiante.objects.get(user_id = id_usuario)
    if request.method == 'POST':
        form = agregarMateria(request.POST, instance= est)
        if form.is_valid():             
            nombre = request.POST['nombre']
            creditos = request.POST['creditos']
            curso = Curso.objects.create(nombre=nombre, creditos=creditos, Estudiante = est)
            return redirect ('/')
    else:
        form=agregarMateria(instance=est)
    context={
            'form':form,
        }
    return render (request, "gestionCursos.html", context)

"""


