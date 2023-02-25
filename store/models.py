from turtle import color
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.utils.safestring import mark_safe

#modelo de PLANTAS DE PRUENAS
class plantas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True)
    descripcion= models.TextField(verbose_name="Descripcion", null= True)

    def __str__(self):
        fila = "nombre: " + self.nombre + " - " + "Descripcion: " + self.descripcion
        return fila

    def delete(self, using=None, keep_parants=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

#TABLAS FUERTES NECESARIAS PARA PLANTAS Y MACETAS
#modelo de MATERIALES macetas
class Material(models.Model):
    nombre_material = models.CharField('Material', max_length=75)

    class meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Material de maceta'
    
    def __str__(self):
        return str(self.id) + '-' + self.nombre_material

#modelo de BENEFICIOS de plantas
class Beneficios(models.Model):
    beneficios = models.CharField('Beneficios', max_length=75)

    class meta:
        verbose_name = 'Beneficios'
        verbose_name_plural = 'Beneficios de la planta'
    
    def __str__(self):
        return str(self.id) + '-' + self.beneficios

#modelo de RECOMENDACIONES de plantas
class Recomendaciones(models.Model):
    recomendaciones = models.CharField('Recomendaciones', max_length=75)

    class meta:
        verbose_name = 'Recomendaciones'
        verbose_name_plural = 'Recomendaciones de la planta'
    
    def __str__(self):
        return str(self.id) + '-' + self.recomendaciones

#modelo de CUIDADOS de plantas
class Cuidados(models.Model):
    cuidados = models.CharField('Cuidados', max_length=150)

    class meta:
        verbose_name = 'Cuidados'
        verbose_name_plural = 'Cuidados de la planta'
    
    def __str__(self):
        return str(self.id) + '-' + self.cuidados

#modelo FOTOS de plantas
class Fotos_plantas(models.Model):
    fotos = models.ImageField(upload_to='imagenes_plantas/', verbose_name="Foto", null=True)

    def image_data(self):
        return format_html(
            '<img src="{}" width="250px"/>',
            self.fotos.url,
        )
    image_data.short_description = u'Foto'
    
    def __str__(self):
        return str(self.id) + 'Fotos: ' + str('<img src="{str(self.fotos)}" width="250px"/>') 
        
    def delete(self, using=None, keep_parants=False):
        self.fotos.storage.delete(self.fotos.name)
        super().delete()

#modelo FOTOS de macetas
class Fotos_macetas(models.Model):

    fotos = models.ImageField(u'fotos', upload_to='imagenes_macetas/',  null=True)

    def delete(self, using=None, keep_parants=False):
        self.fotos.storage.delete(self.fotos.name)
        super().delete()

#modelo de COLORES para macetas y plantas
class Color(models.Model):
    colores = models.CharField('Color', max_length=30)

    class meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Color de la planta'
    
    def __str__(self):
        return str(self.id) + '-' + self.colores

#modelo de CATEGORIAS de plantas
class Categoria(models.Model):
    nombre_categoria = models.CharField(verbose_name=_('nombre de la cantegoria del producto'), max_length=75)
    fotos = models.ImageField(upload_to='imagenes_categorias/', verbose_name="Foto", null=True)

    class Meta:
        verbose_name = 'Categoria plantas'
        verbose_name_plural = 'Categorias y subcategorias de plantas'
        ordering = ['-nombre_categoria']
    
    def image_data(self):
        return format_html(
            '<img src="{}" width="250px"/>',
            self.fotos.url,
        )
    image_data.short_description = u'Foto'
    
    def __str__(self):
        return str(self.id) + '-' + self.nombre_categoria + 'Fotos: ' + str('<img src="{str(self.fotos)}" width="250px"/>') 

    def delete(self, using=None, keep_parants=False):
        self.fotos.storage.delete(self.fotos.name)
        super().delete()


#modelo de SUBCATEGORIA para plantas
class SubCategoria(models.Model):
    nombre_sub_categoria = models.CharField(max_length=40, blank=True, null=True)
    categoria = models.ForeignKey(
        'Categoria',
        verbose_name='categoriaS',
        on_delete=models.CASCADE,
        blank=True, null=True)

    class meta:
        verbose_name = 'nombre_sub_categoria'
        verbose_name_plural = 'Sub categoria de planta'
    
    def __str__(self):
        return 'Sub categoria: ' + self.nombre_sub_categoria + ', ' + 'Categoria: ' +  str(self.categoria.nombre_categoria)

#modelo de PLANTASFINAL
class plantas_final(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_planta = models.CharField(max_length=100, verbose_name='nombre_planta')

    colgante__colgante = (
        ('0', 'COLAGANTE'),
        ('1', 'NO COLGANTE'),
    )
    colgante_no_colgante = models.CharField(
        'Colgante o no colgante', 
        max_length=1, 
        choices=colgante__colgante
    )

    interior__exterior = (
        ('0', 'INTERIOR'),
        ('1', 'EXTERIOR'),
        ('2', 'AMBOS'),
    )
    interior_no_interior = models.CharField(
        'Interior o no exterior', 
        max_length=1, 
        choices=interior__exterior
    )

    precio = models.FloatField(null=True)
    descripcion= models.TextField(verbose_name="Descripcion", null= True)
    imagen_portada = models.ImageField(upload_to='imagenes_portada/', verbose_name="Imagen", null=True)
    sub_categoria = models.ForeignKey(
        SubCategoria,
        verbose_name='categoria',
        on_delete=models.CASCADE,
        blank=True, null=True)
    
    beneficios = models.ManyToManyField(
        Beneficios,
        through='Planta_beneficio',
        blank=True,
    )

    recomendaciones = models.ManyToManyField(
        Recomendaciones,
        through='Planta_recomendacion',
        blank=True,
    )

    cuidados = models.ManyToManyField(
        Cuidados,
        through='Planta_cuidado',
        blank=True,
    )
    fotos = models.ManyToManyField(
        Fotos_plantas,
        through='Planta_foto',
        blank=True,
    )

    colores = models.ManyToManyField(
        Color,
        through='Planta_color',
        blank=True,
    )

    def __str__(self):
        fila = "nombre: " + self.nombre_planta + " - " + "Descripcion: " + self.descripcion
        return fila

    def delete(self, using=None, keep_parants=False):
        self.imagen_portada.storage.delete(self.imagen_portada.name)
        super().delete()
    
#1.1 modelo para planta  PLANTA BENEFICIO
class Planta_beneficio(models.Model):
    plantas = models.ForeignKey(
        plantas_final, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    beneficio = models.ForeignKey(
        Beneficios, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    class meta:
        db_table = 'planta_planta_habilidades'
        verbose_name = 'Beneficio planta'
        verbose_name_plural = 'Beneficios planta'
    
    def __str__(self):
        return self.beneficio.beneficios

#1.2 modelo para planta  PLANTA RECOMENDACION
class Planta_recomendacion(models.Model):
    plantas = models.ForeignKey(
        plantas_final, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    recomendacion = models.ForeignKey(
        Recomendaciones, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    class meta:
        db_table = 'planta_planta_recomendaciones'
        verbose_name = 'Recomendacion planta'
        verbose_name_plural = 'Recomendaciones planta'
    
    def __str__(self):
        return self.recomendacion.recomendaciones

#1.3 modelo para planta  PLANTA CUIDADOS
class Planta_cuidado(models.Model):
    plantas = models.ForeignKey(
        plantas_final, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    cuidado = models.ForeignKey(
        Cuidados, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    class meta:
        db_table = 'planta_planta_cuidados'
        verbose_name = 'Cuidado planta'
        verbose_name_plural = 'Cuidados planta'
    
    def __str__(self):
        return self.cuidado.cuidados

#1.4 modelo para planta  PLANTA FOTOS
class Planta_foto(models.Model):
    plantas = models.ForeignKey(
        plantas_final, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    foto = models.ForeignKey(
        Fotos_plantas, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    class meta:
        db_table = 'planta_planta_fotos'
        verbose_name = 'Foto planta'
        verbose_name_plural = 'Fotos planta'

    def image_preview(self):
        if self.foto.fotos:
            return mark_safe('<img src="{0}" width="150" height="150" />'.format(self.foto.fotos.url))
        else:
            return '(No image)'
            
    def __str__(self):
        return str(self.foto.id)

#1.5 modelo para planta  PLANTA COLOR
class Planta_color(models.Model):
    plantas = models.ForeignKey(
        plantas_final, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    color = models.ForeignKey(
        Color, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    class meta:
        db_table = 'planta_planta_colores'
        verbose_name = 'Color planta'
        verbose_name_plural = 'Colores planta'
    
    def __str__(self):
        return str(self.color.id)

#modelo MACETAS_final 
class macetas_final(models.Model):
    nombre_maceta = models.CharField(max_length=100, verbose_name='nombre_maceta')
    descripcion= models.TextField(verbose_name="Descripcion", null= True)
    precio = models.FloatField(null=True)
    imagen_portada = models.ImageField(upload_to='imagenes_portada_maceta/', verbose_name="Imagen", null=True)
    material = models.ForeignKey(
        Material,
        verbose_name='material de maceta',
        on_delete=models.CASCADE,
        blank=True, null=True)

    colores = models.ManyToManyField(
        Color,
        through='Maceta_color',
        blank=True,
    )

    def __str__(self):
        fila = "nombre: " + self.nombre_maceta + " - " + "Descripcion: " + self.descripcion
        return fila

    def delete(self, using=None, keep_parants=False):
        self.imagen_portada.storage.delete(self.imagen_portada.name)
        super().delete()

#1.1 modelo para maceta  MACETA COLORES
class Maceta_color(models.Model):
    macetas = models.ForeignKey(
        macetas_final, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    color = models.ForeignKey(
        Color, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    class meta:
        db_table = 'maceta_maceta_colores'
        verbose_name = 'Color maceta'
        verbose_name_plural = 'Colores maceta'
    
    def __str__(self):
        return self.color.colores

#1.2 modelo para maceta MACETA FOTOS
class Maceta_foto(models.Model):
    macetas = models.ForeignKey(
        macetas_final, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    foto = models.ForeignKey(
        Fotos_macetas, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    class meta:
        db_table = 'maceta_maceta_fotos'
        verbose_name = 'Foto maceta'
        verbose_name_plural = 'Fotos maceta'
    
    def image_preview(self):
        if self.foto.fotos:
            return mark_safe('<img src="{0}" width="150" height="150" />'.format(self.foto.fotos.url))
        else:
            return '(No image)'

    def __str__(self):
        return str(self.foto.id)

#modelo  de producto MACETA y PLANTA 
class plantas_macetas_final(models.Model):
    id = models.AutoField(primary_key=True)
    alto = models.FloatField(null=True, verbose_name="Alto de la maceta y planta juntas")
    ancho = models.FloatField(null=True, verbose_name="Ancho de la maceta y planta junta")
    largo = models.FloatField(null=True, verbose_name="Largo de la maceta y planta junta")

    planta = models.ForeignKey(
        plantas_final,
        verbose_name='Planta del producto',
        on_delete=models.CASCADE,
        blank=True, null=True)

    maceta = models.ForeignKey(
        macetas_final,
        verbose_name='Maceta del producto',
        on_delete=models.CASCADE,
        blank=True, null=True)

    def __str__(self):
        fila = str(self.id) + " - " + "Alto: " + self.alto + " - " + "Ancho: " + self.ancho + " - " + "Largo: " + self.largo
        return fila