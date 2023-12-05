from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpRequest
from django.db.models import Q


# -------- YA ESTA ----
@login_required
def menu(request):
    # persona_list=Persona.objects.all()
    # context={"persona_list":persona_list}
    return render(request,'plantilla/menu.html')
    # return render(request,'plantilla/menu.html')


def registro(request):
    return render(request,'plantilla/perfilusu.html')


# -------- YA ESTA ----
def perfil(request):
    return render(request,'plantilla/perfilusu.html')


# -------- YA ESTA ----
def contactar(request):
    return render(request,'plantilla/contactanos.html')

# -------- YA ESTA ----
def nosotros(request):
    return render(request,'plantilla/nosotros.html')

# -------- YA ESTA ----
def detalles(request):
    return render(request,'plantilla/detalle.html')

# -------- YA ESTA ----
def mapa(request):
    return render(request,'plantilla/mapa.html')



def calificacion(request):
    return render(request,'plantilla/contactanos.html')

def busqueda(request):
    return render(request,'plantilla/contactanos.html')