# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DiscadorOcorrencia(models.Model):
    carteira = models.TextField()
    sist = models.ForeignKey('Sistema', models.DO_NOTHING, db_column='SIST', related_name='sistemas')  # Field name made lowercase.
    ocorrencia = models.IntegerField()
    alo = models.IntegerField()
    cpc = models.IntegerField()

    class Meta:
        db_table = 'DISCADOR_OCORRENCIA'


class Sistema(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome_sistema = models.TextField(unique=True)

    class Meta:
        db_table = 'SISTEMA'

    def __str__(self):
        return self.nome_sistema
