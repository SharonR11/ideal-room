from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.menu, name='menu'),
    # -------- YA ESTA ----
    path('perfil/', views.perfil, name='perfil'),

    # -------- } ----
    path('login/',views.login,name='login'),
    path('registrar/',views.registro,name='registrar'),
    # -------- YA ESTA ----
    path('contacto/', views.contactar, name='contacto'),
    # -------- YA ESTA ----
    path('nosotros/',views.nosotros, name='nosotros'),
    # -------- YA ESTA ----
    path('detalle/', views.detalles, name='detalle'),
    # -------- YA ESTA ----
    path('mapa/',views.mapa,name='mapa'),
    # -------- ----
    path('calificacion/',views.calificacion, name='calificacion'),
]