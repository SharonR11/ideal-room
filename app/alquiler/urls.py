from django.urls import path
from . import views

urlpatterns = [

    path('', views.menu, name='menu'),
    path('perfil', views.perfil, name='perfil'),
    # path('registrar/',views.insertarpersona,name='registrar'),
    # path('eliminar/<idPersona>/', views.eliminar, name='eliminar'),
    # path('data/<int:idPersona>',views.datapersona, name='data'),
    # path('modificar/<int:idPersona>/', views.editar, name='editar'),
    # path('buscar/',views.buscar,name='buscar'),
    # path('perfil/<int:idPersona>',views.perfil, name='perfil'),
]