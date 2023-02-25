from django.urls import path
from . import views

from django.contrib import admin

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [

    path('', views.inicio_def, name='ver_categoria_def_path'),
    path('inicio/', views.inicio_def, name='ver_categoria_def_path'),
    path('nosotros/', views.nosotros_def),
    path('plantas/', views.plantas_def, name='ver_planta_def_path'),
    path('plantas/crear/', views.crear_planta_def, name='crear_planta_def_path'),
    path('plantas/editar/', views.editar_planta_def, name='editar_planta_def_path'),
    path('eliminar/<int:id>', views.eliminar_planta_def, name='eliminar_planta_def_path'),
    path('plantas/editar/<int:id>', views.editar_planta_def, name='editar_planta_def_path'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Administracion de Kaktus'