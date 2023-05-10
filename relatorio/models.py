# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Carteira(models.Model):
    cod_carteira = models.AutoField(primary_key=True)
    nome_carteira = models.TextField(unique=True)

    class Meta:
        db_table = 'CARTEIRA'

    def __str__(self):
        return self.nome_carteira


class DiscadorOcorrencia(models.Model):
    sist = models.ForeignKey('Sistema', on_delete=models.CASCADE, db_column='SIST')  # Field name made lowercase.
    carteira = models.ForeignKey(Carteira, on_delete=models.CASCADE, db_column='carteira')
    ocorrencia = models.ForeignKey('Ocorrencia', on_delete=models.CASCADE, db_column='ocorrencia')
    alo = models.IntegerField()
    cpc = models.IntegerField()
    promessa = models.IntegerField()

    class Meta:
        db_table = 'DISCADOR_OCORRENCIA'


class Ocorrencia(models.Model):
    pk_interna = models.AutoField(primary_key=True)
    num_ocorrencia = models.IntegerField(unique=True)
    desc_ocorrencia = models.TextField(unique=True)

    class Meta:
        db_table = 'OCORRENCIA'

    def __str__(self):
        return self.desc_ocorrencia

class Sistema(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome_sistema = models.TextField(unique=True)

    class Meta:
        db_table = 'SISTEMA'

    def __str__(self):
        return self.nome_sistema