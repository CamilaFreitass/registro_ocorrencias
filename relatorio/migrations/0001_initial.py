# Generated by Django 4.1.4 on 2023-07-29 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carteira',
            fields=[
                ('cod_carteira', models.AutoField(primary_key=True, serialize=False)),
                ('nome_carteira', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'CARTEIRA',
            },
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('pk_interna', models.AutoField(primary_key=True, serialize=False)),
                ('num_ocorrencia', models.IntegerField(unique=True)),
                ('desc_ocorrencia', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'OCORRENCIA',
            },
        ),
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nome_sistema', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'SISTEMA',
            },
        ),
        migrations.CreateModel(
            name='DiscadorOcorrencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alo', models.IntegerField()),
                ('cpc', models.IntegerField()),
                ('promessa', models.IntegerField()),
                ('carteira', models.ForeignKey(db_column='carteira', on_delete=django.db.models.deletion.CASCADE, to='relatorio.carteira')),
                ('ocorrencia', models.ForeignKey(db_column='ocorrencia', on_delete=django.db.models.deletion.CASCADE, to='relatorio.ocorrencia')),
                ('sist', models.ForeignKey(db_column='SIST', on_delete=django.db.models.deletion.CASCADE, to='relatorio.sistema')),
            ],
            options={
                'db_table': 'DISCADOR_OCORRENCIA',
            },
        ),
    ]
