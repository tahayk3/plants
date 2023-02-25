from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

#modelos para CRUD de plantas de prueba
from . models import Maceta_foto, Planta_cuidado, Planta_foto, Planta_recomendacion, plantas
#modelos fuertes para macetas
from . models import Material,Recomendaciones, Cuidados, Color, Categoria, Fotos_plantas
#modelos fuertes para plantas
from . models import Beneficios
#modelos necesarios para plantas
from . models import SubCategoria, Planta_beneficio, Planta_recomendacion, Planta_cuidado, Planta_color
#modelos necesarios para macetas
from . models import Maceta_color, Fotos_macetas
#modelos de pruebas
#modelos finales
from . models import plantas_final, macetas_final, plantas_macetas_final

#PLANTAS
class SubAdminInline(admin.TabularInline):
    extra = 1
    model = SubCategoria

class CategoriaModelAdmin(admin.ModelAdmin):
    inlines = (SubAdminInline,)
    search_fields = ('nombre_categoria',)
    list_filter = ('nombre_categoria',)
    list_display = ('id', 'nombre_categoria','image_data')

class SubCategoriaModelAdmin(admin.ModelAdmin):
    autocomplete_fields = ["categoria"]
    search_fields = ('nombre_sub_categoria',)
    list_filter = ('nombre_sub_categoria',)

class BeneficioPlantaInline(admin.TabularInline):
    model = Planta_beneficio
    extra = 1
    autocomplete_fields = ['beneficio']

class BeneficiosAdmin(admin.ModelAdmin):
    inlines = (BeneficioPlantaInline,)
    search_fields = ('beneficios'),
    ordering = ['beneficios']

class RecomendacionPlantaInline(admin.TabularInline):
    model = Planta_recomendacion
    extra = 1
    autocomplete_fields = ['recomendacion']

class RecomendacionesAdmin(admin.ModelAdmin):
    inlines = (RecomendacionPlantaInline,)
    search_fields = ('recomendaciones'),
    ordering = ['recomendaciones']

class CuidadoPlantaInline(admin.TabularInline):
    model = Planta_cuidado
    extra = 1
    autocomplete_fields = ['cuidado']

class CuidadosAdmin(admin.ModelAdmin):
    inlines = (CuidadoPlantaInline,)
    search_fields = ('cuidados'),
    ordering = ['cuidados']

class FotoPlantaInline(admin.TabularInline):
    model = Planta_foto
    extra = 1
    autocomplete_fields = ['foto']
    readonly_fields = ('image_preview',)

class FotosAdmin(admin.ModelAdmin):
    inlines = (FotoPlantaInline,)
    search_fields = ('fotos'),
    ordering = ['fotos']
    list_display = ('id', 'image_data')

class ColorMacetaInline(admin.TabularInline):
    model = Maceta_color
    extra = 1
    autocomplete_fields = ['color']

class ColorPlantaInline(admin.TabularInline):
    model = Planta_color
    extra = 1
    autocomplete_fields = ['color']

class ColoresAdmin(admin.ModelAdmin):
    inlines = (ColorMacetaInline, ColorPlantaInline,)
    search_fields = ('colores'),
    ordering = ['colores']

class PlantasModelAdmin(admin.ModelAdmin):
    def foto_portada(self, obj):
        return format_html('<img src={} width="130" heiht="100" />', obj.imagen_portada.url)
    list_display = (
        'id',
        'nombre_planta',
        'colgante_no_colgante',
        'interior_no_interior',
        'precio',
        'descripcion',
        'foto_portada',
        'sub_categoria',
    )

    inlines = [BeneficioPlantaInline,RecomendacionPlantaInline,CuidadoPlantaInline,FotoPlantaInline, ColorPlantaInline,]
    search_fields = ('beneficios'),
    ordering = ['beneficios']

admin.site.register(Material)
admin.site.register(Cuidados, CuidadosAdmin)
admin.site.register(Fotos_plantas, FotosAdmin)
admin.site.register(Beneficios, BeneficiosAdmin)
admin.site.register(Categoria, CategoriaModelAdmin)
admin.site.register(plantas_final, PlantasModelAdmin)
admin.site.register(SubCategoria, SubCategoriaModelAdmin)
admin.site.register(Recomendaciones, RecomendacionesAdmin)

#MACETAS
class FotoMacetaInline(admin.TabularInline):
    model = Maceta_foto
    extra = 1
    autocomplete_fields = ['foto']
    readonly_fields = ('image_preview',)

class Fotos2Admin(admin.ModelAdmin):
    inlines = (FotoMacetaInline,)
    search_fields = ('fotos'),
    ordering = ['fotos']

    def foto(self, obj):
        return format_html('<img src={} width="130" heiht="100" />', obj.fotos.url)
    list_display = ('id', 'foto')

class MacetasModelAdmin(admin.ModelAdmin):
    def foto_portada(self, obj):
        return format_html('<img src={} width="130" heiht="100" />', obj.imagen_portada.url)
    list_display = (
        'id',
        'nombre_maceta',
        'descripcion',
        'precio',
        'foto_portada',
        'material',
    )
    inlines = [ColorMacetaInline, FotoMacetaInline, ]
    search_fields = ('colores'),
    ordering = ['colores']

admin.site.register(Color, ColoresAdmin)
admin.site.register(plantas_macetas_final)
admin.site.register(Fotos_macetas, Fotos2Admin)
admin.site.register(macetas_final,MacetasModelAdmin)

#PRUEBAS
admin.site.register(plantas)





