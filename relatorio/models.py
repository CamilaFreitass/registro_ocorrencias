from django.db import models


class Carteira(models.Model):
    cod_carteira = models.AutoField(primary_key=True)
    nome_carteira = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'CARTEIRA'

    def __str__(self):
        return self.nome_carteira


class Ocorrencia(models.Model):
    pk_interna = models.AutoField(primary_key=True)
    num_ocorrencia = models.IntegerField(unique=True)
    desc_ocorrencia = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'OCORRENCIA'

    def __str__(self):
        return self.desc_ocorrencia


class Sistema(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome_sistema = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'SISTEMA'

    def __str__(self):
        return self.nome_sistema


class DiscadorOcorrencia(models.Model):
    sist = models.ForeignKey(Sistema, on_delete=models.CASCADE, db_column='SIST')  # Field name made lowercase.
    carteira = models.ForeignKey(Carteira, on_delete=models.CASCADE, db_column='carteira')
    ocorrencia = models.ForeignKey(Ocorrencia, on_delete=models.CASCADE, db_column='ocorrencia')
    alo = models.IntegerField()
    cpc = models.IntegerField()
    promessa = models.IntegerField()

    class Meta:
        db_table = 'DISCADOR_OCORRENCIA'