from django.db import models
from django_earthdistance.models import EarthDistanceQuerySet
from django_earthdistance.models import EarthDistance, LlToEarth
from django.db.models.fields import SmallIntegerField



class Usuario(models.Model):
     
    id = models.AutoField(primary_key=True,db_column='usuario_id')
    nombre = models.CharField(max_length=100, blank=True, db_column='nombre')
    apellido = models.CharField(max_length=100, blank=True, db_column='apellido')
    email = models.CharField(max_length=50, blank=True, db_column='email')
    facebook_id = models.CharField(max_length=20, blank=True, db_column='facebook_id')
    estado = models.SmallIntegerField(blank=True, null=True, db_column='estado') 
    telefono = models.CharField(max_length=20, blank=True, db_column='telefono')
    fecha_registro = models.DateTimeField(blank=True, null=True, db_column='fecha_registro')
    direccion = models.CharField(max_length=120, null=True, blank=True,db_column='direccion')
    foto_perfil_url = models.CharField(max_length=150, null=True, blank=True,db_column='foto_perfil_url')
    notify_id = models.CharField(max_length=150, null=True, blank=True,db_column='notify_id')
 
     
     
    class Meta:
        managed = True
        db_table = 'usuario'
        ordering = ('id',)

    def __unicode__(self):
        return '%s' % (self.id)


class TipoMascota(models.Model):
    id = models.AutoField(primary_key=True,db_column='tipo_id')
    tipo = models.CharField(max_length=20, blank=True, db_column='tipo')
        

    class Meta:
        managed = True
        db_table = 'tipo_mascota'
        ordering = ('id',)
            
            
    def __unicode__(self):
        return '%s' % (self.tipo)


class Mascota(models.Model):
    
    id = models.AutoField(primary_key=True,db_column='mascota_id')
    nombre = models.CharField(max_length=50, blank=True, db_column='nombre')
    raza = models.CharField(max_length=50, blank=True, db_column='raza')
    tipo = models.ForeignKey(TipoMascota, db_column='fk_tipo', blank=True, null=True, unique=False)
    sexo = models.CharField(max_length=50, blank=True, db_column='sexo')
    edad = SmallIntegerField(blank=True, null=True, db_column='edad')
    tamanio = models.CharField(max_length=50, blank=True, db_column='tamanio')
    compatible_chicos = models.SmallIntegerField(blank=True, null=True, db_column='compatible_chicos')
    medicacion = models.SmallIntegerField(blank=True, null=True, db_column='medicacion')

     
    class Meta:
        managed = True
        db_table = 'mascota'
        ordering = ('id',)
       
  

class TipoAviso(models.Model):
    id = models.AutoField(primary_key=True,db_column='tipo_id')
    tipo = models.CharField(max_length=50, blank=True, db_column='tipo')
        

    class Meta:
        managed = True
        db_table = 'tipo_aviso'
        ordering = ('id',)

    def __unicode__(self):
        return '%s' % (self.tipo)

        
class Publicacion(models.Model):
    
    id = models.AutoField(primary_key=True,db_column='publicacion_id')
    mascota = models.ForeignKey(Mascota, db_column='fk_mascota', blank=True, null=True)
    usuario = models.ForeignKey(Usuario, db_column='fk_usuario', blank=True, null=True)
    aviso = models.ForeignKey(TipoAviso, db_column='fk_aviso', blank=True, null=True)
    en_transito = models.CharField(max_length=1, blank=True,db_column='en_transito')
    fecha_publicacion = models.DateTimeField(blank=True, null=True, db_column='fecha_publicacion')
    estado = models.SmallIntegerField(blank=True, null=True, db_column='estado')
    latitud = models.FloatField(blank=True, null=True, db_column='latitud')
    longitud = models.FloatField(blank=True, null=True, db_column='longitud')
    descripcion = models.TextField(blank=True, null=True, db_column='descripcion')
    
    objects = EarthDistanceQuerySet.as_manager()
     
    class Meta:
        managed = True
        db_table = 'publicacion'
        ordering = ('-fecha_publicacion','-id',)

    def __unicode__(self):
        return '%s' % (self.id)
        
        
class MultimediaMascota(models.Model):
    id = models.AutoField(primary_key=True,db_column='multimediamascota_id')
    id_publicacion = models.ForeignKey(Publicacion, db_column='fk_publicacion', blank=True, null=True, related_name='multimedia')
    tipo = models.CharField(max_length=50, blank=True, db_column='tipo')
    url = models.CharField(max_length=150, null=True, blank=True,db_column='url')
    orden = models.SmallIntegerField(blank=True, null=True, db_column='orden')
    
    class Meta:
        managed = True
        db_table = 'multimedia_mascota'
        ordering = ('id','id_publicacion','orden')
    
    
class Mensaje(models.Model):
    id = models.AutoField(primary_key=True,db_column='mensaje_id')
    id_publicacion = models.ForeignKey(Publicacion, db_column='fk_publicacion', blank=True, null=True, related_name='mensajes')
    usuario = models.ForeignKey(Usuario, db_column='fk_usuario', blank=True, null=True)
    fecha_publicacion = models.DateTimeField(blank=True, null=True, db_column='fecha_publicacion')
    texto = models.TextField(blank=True, null=True, db_column='texto')
    
    class Meta:
        managed = True
        db_table = 'mensaje'
        ordering = ('id',)


class Adopcion(models.Model):
    id = models.AutoField(primary_key=True, db_column='adopcion_id')
    publicacion = models.ForeignKey('Publicacion', db_column='fk_publicacion')
    usuario = models.ForeignKey('Usuario', db_column='fk_usuario')
    fecha_pedido = models.DateTimeField(blank=True, null=True, db_column='fecha_pedido')
    concretada = models.SmallIntegerField(blank=True, null=True, default=0,db_column='concretada')
    
    class Meta:
        managed = True
        db_table = 'adopcion'
        ordering = ('-fecha_pedido',)
    
    