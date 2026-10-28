"""
URL configuration for pikhobazar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

# Un solo bloque unificado
urlpatterns = [

    path('gestion/creacion/', views.crear_producto, name='crear_producto'),
    path('gestion/modificion/<str:codigo>/', views.editar_producto, name='editar_producto'),
    path('gestion/eliminacion/<str:codigo>/', views.eliminar_producto, name='eliminar_producto'),

    # 2. Deja el admin y el index al final de las rutas de gestión
    path('admin/', admin.site.urls),
    
    # 3. Esta ruta es la que te está "atrapando". Déjala después de las específicas.
    path('', views.index, name='home'), 
    
    path("index/", views.index, name="index"),
    
    
    path("index/", views.index, name="index"),
    path("baño/", views.baño, name="baño"),
    path("cocina/", views.cocina, name="cocina"),
    path("combos/", views.combos, name="combos"),
    path("deco/", views.deco, name="deco"),
    
    
    path('producto/<str:codigo>/', views.detalle_producto, name='producto'),
    

    # Rutas para las páginas de cocina
    path("Asaderas_Rectangulares/", views.Asaderas_Rectangulares, name="Asaderas_Rectangulares"),
    path("Bowl_Breakfast/", views.Bowl_Breakfast, name="Bowl_Breakfast"),
    path("Budineras/", views.Budineras, name="Budineras"),
    path("Cacerola/", views.Cacerola, name="Cacerola"),
    path("Ensaladeras/", views.Ensaladeras, name="Ensaladeras"),
    path("Flaneras/", views.Flaneras, name="Flaneras"),
    path("Fuentes/", views.Fuentes, name="Fuentes"),
    path("Jarro_Breakfast/", views.Jarro_Breakfast, name="Jarro_Breakfast"),
    path("Manteles_individuales/", views.Manteles_individuales, name="Manteles_individuales"),
    path("Molde_de_Galletitas/", views.Molde_de_Galletitas, name="Molde_de_Galletitas"),
    path("Molde_Muffins/", views.Molde_Muffins, name="Molde_Muffins"),
    path("Pizzeras/", views.Pizzeras, name="Pizzeras"),
    path("Planchas_Biferas/", views.Planchas_Biferas, name="Planchas_Biferas"),
    path("por_mayor/", views.por_mayor, name="por_mayor"),
    path("Sartenes/", views.Sartenes, name="Sartenes"),
    path("Servilleteros/", views.Servilleteros, name="Servilleteros"),
    path("Tapers/", views.Tapers, name="Tapers"),
    path("Tarteras/", views.Tarteras, name="Tarteras"),
    path("Taza_Flashy/", views.Taza_Flashy, name="Taza_Flashy"),
    path("Tazas_Mocha/", views.Tazas_Mocha, name="Tazas_Mocha"),
    path("Utensillos/", views.Utensillos, name="Utensillos"),
    path("Wok/", views.Wok, name="Wok"),

    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)