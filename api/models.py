from django.db import models

class Usuario(models.Model):
    
    id = models.AutoField(primary_key=True,db_column='usuario_id')
    email = models.CharField(max_length=50, blank=True,db_column='email')
    facebook_id = models.CharField(max_length=20, blank=True,db_column='facebook_id')
    estado = models.SmallIntegerField(blank=True, null=True,db_column='estado') 
    telefono = models.CharField(max_length=20, blank=True,db_column='telefono')
    fecha_registro = models.DateField(blank=True, null=True,db_column='fecha_registro')
    direccion = models.CharField(max_length=120, blank=True,db_column='direccion')
    
    
    class Meta:
        managed = True
        db_table = 'usuario'
        ordering = ('id',)