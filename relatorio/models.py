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
    ocorrencia = models.OneToOneField('Ocorrencia', on_delete=models.CASCADE, db_column='ocorrencia')
    carteira = models.ForeignKey(Carteira, on_delete=models.CASCADE, db_column='carteira')
    alo = models.IntegerField()
    cpc = models.IntegerField()
    promessa = models.IntegerField()

    class Meta:
        db_table = 'DISCADOR_OCORRENCIA'


class Ocorrencia(models.Model):
    num_ocorrencia = models.IntegerField(primary_key=True)
    desc_ocorrencia = models.TextField()

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
