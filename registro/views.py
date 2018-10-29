from django.shortcuts import render
from django.http import HttpResponse
from .models import Postulante
from django.shortcuts import redirect

# Create your views here.


#importar user
from django.contrib.auth.models import User
#sistema de autenticación 
from django.contrib.auth import authenticate,logout, login as auth_login
from django.contrib.auth.decorators import login_required


def index(request):
    usuario = request.session.get('usuario',None)
    return render(request,'index.html',{'nombre':"Duoc",'elementos':["one", "two", "three"],'postulantes':Postulante.objects.all()})

def registro(request):
    return render(request, 'formulario.html',{})

def crear(request):
    run = request.POST.get('run','')
    nombre = request.POST.get('nombre','')
    fecha = request.POST.get('fechaNacimiento','')
    correo = request.POST.get('correo','')
    telefono = request.POST.get('telefono','')
    region = request.POST.get('region','')
    comuna = request.POST.get('comuna','')
    vivienda = request.POST.get('tipoVivienda','')

    postulante = Postulante(run=run, nombre=nombre, fecha=fecha, correo=correo, telefono=telefono, region=region, comuna=comuna, vivienda=vivienda)
    postulante.save()
    
    return render(request,'index.html')
    
def login(request):
    return render(request,'login.html',{})

def login_iniciar(request):
    usuario = request.POST.get('nombre_usuario','')
    contrasenia = request.POST.get('password','')
    user = authenticate(request,username=usuario, password=contrasenia)

    if user is not None:
        auth_login(request, user)
        request.session['usuario'] = user.first_name+" "+user.last_name
        return redirect("index")
    else:
        return redirect("login")

@login_required(login_url='login')
def cerrar_session(request):
    del request.session['usuario']
    logout(request)
    return redirect('index')