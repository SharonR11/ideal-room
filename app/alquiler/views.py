from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpRequest
from django.db.models import Q

@login_required
def menu(request):
    # persona_list=Persona.objects.all()
    # context={"persona_list":persona_list}
    return render(request,'plantilla/menu.html')
    # return render(request,'plantilla/menu.html')

def insertarpersona(request):
    return redirect('/')