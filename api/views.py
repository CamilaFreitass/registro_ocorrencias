from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from relatorio.models import DiscadorOcorrencia, Sistema, Carteira, Ocorrencia
from django.http import QueryDict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core import serializers
from django.http import JsonResponse
from relatorio.templatetags.extras import get_values


#################Geral##########################

@api_view()
def lista_classificacao(request):
    busca = request.GET.get('buscar')
    querystring = request.META['QUERY_STRING']
    querydict = QueryDict(querystring).dict()
    buscar = querydict.get('buscar')
    ordenar = querydict.get('ordenar')
    urlx = request.GET.get("ordenar")
    if busca:
        lista_registros = (DiscadorOcorrencia.objects.filter(sist__nome_sistema__icontains=busca) |
                            DiscadorOcorrencia.objects.filter(carteira__nome_carteira__icontains=busca) |
                            DiscadorOcorrencia.objects.filter(ocorrencia__num_ocorrencia__icontains=busca))
        dados = {'registros': lista_registros, 'buscar': buscar}
        if ordenar:
            lista_registros = (DiscadorOcorrencia.objects.filter(sist__nome_sistema__icontains=busca) |
                                DiscadorOcorrencia.objects.filter(carteira__nome_carteira__icontains=busca).order_by(ordenar) |
                                DiscadorOcorrencia.objects.filter(ocorrencia__num_ocorrencia__icontains=busca).order_by(ordenar))

            dados = {'registros': lista_registros, 'buscar': buscar, 'ordenar': ordenar}
    elif ordenar:
        lista_registros = DiscadorOcorrencia.objects.order_by(ordenar)
        dados = {'registros': lista_registros, 'ordenar': ordenar}
    else:
        lista_registros = DiscadorOcorrencia.objects.all()
        dados = {'registros': lista_registros}

    ''' PK '''
    if dados['registros']:
        registro = dados['registros'][0]
        dados['pk'] = registro._meta.db_returning_fields[0].name
        dados['columns'] = [x.name for x in registro._meta.get_fields() if x.concrete]

    ''' URL '''
    dados['urlx'] = urlx
    dados['registros'] = [{col: get_values(registro, col) for col in dados['columns']} for registro in dados['registros']]
    return JsonResponse(dados)


@api_view()
def delete_classificacao(request, id):
    try:
        classificacao = get_object_or_404(DiscadorOcorrencia, pk=id)
        classificacao.delete()
        return HttpResponse(status=204)
    except:
        return HttpResponse(status=404)


#################Sistema##########################

@api_view()
def lista_sistema(request):
    busca = request.GET.get('buscar')
    querystring = request.META['QUERY_STRING']
    querydict = QueryDict(querystring).dict()
    buscar = querydict.get('buscar')
    ordenar = querydict.get('ordenar')
    urlx = request.GET.get('ordenar')
    if busca:
        lista_registros = (Sistema.objects.filter(codigo__icontains=busca) |
                        Sistema.objects.filter(nome_sistema__icontains=busca))
        dados = {'registros': lista_registros, 'buscar': buscar}
        if ordenar:
            lista_registros = (Sistema.objects.filter(codigo__icontains=busca).order_by(ordenar) |
                               Sistema.objects.filter(nome_sistema__icontains=busca).order_by(ordenar))
            dados = {'registros': lista_registros, 'buscar': buscar, 'ordenar': ordenar}
    elif ordenar:
        lista_registros = Sistema.objects.order_by(ordenar)
        dados = {'registros': lista_registros, 'ordenar': ordenar}
    else:
        lista_registros = Sistema.objects.all()
        dados = {'registros': lista_registros}

    ''' PK '''
    if dados['registros']:
        registro = dados['registros'][0]
        dados['pk'] = registro._meta.db_returning_fields[0].name
        dados['columns'] = [x.name for x in registro._meta.get_fields() if x.concrete]

    ''' URL '''
    dados['urlx'] = urlx
    dados['registros'] = [{col: get_values(registro, col) for col in dados['columns']} for registro in dados['registros']]
    return JsonResponse(dados)


@api_view()
def delete_sistema(request, codigo):
    try:
        sistema = get_object_or_404(Sistema, pk=codigo)
        sistema.delete()
        return HttpResponse(status=204)
    except:
        return HttpResponse(status=404)

#################Carteira##########################

@api_view()
def lista_carteira(request):
    busca = request.GET.get('buscar')
    querystring = request.META['QUERY_STRING']
    querydict = QueryDict(querystring).dict()
    buscar = querydict.get('buscar')
    ordenar = querydict.get('ordenar')
    urlx = request.GET.get("ordenar")
    if busca:
        lista_registros = (Carteira.objects.filter(cod_carteira__icontains=busca) |
                        Carteira.objects.filter(nome_carteira__icontains=busca))
        dados = {'registros': lista_registros, 'buscar': buscar}
        if ordenar:
            lista_registros = (Carteira.objects.filter(cod_carteira__icontains=busca).order_by(ordenar) |
                               Carteira.objects.filter(nome_carteira__icontains=busca).order_by(ordenar))
            dados = {'registros': lista_registros, 'buscar': buscar, 'ordenar': ordenar}
    elif ordenar:
        lista_registros = Carteira.objects.order_by(ordenar)
        dados = {'registros': lista_registros, 'ordenar': ordenar}
    else:
        lista_registros = Carteira.objects.all()
        dados = {'registros': lista_registros}

    ''' PK '''
    if dados['registros']:
        registro = dados['registros'][0]
        dados['pk'] = registro._meta.db_returning_fields[0].name
        dados['columns'] = [x.name for x in registro._meta.get_fields() if x.concrete]

    ''' URL '''
    dados['urlx'] = urlx
    dados['registros'] = [{col: get_values(registro, col) for col in dados['columns']} for registro in dados['registros']]
    return JsonResponse(dados)


@api_view()
def delete_carteira(request, cod_carteira):
    try:
        carteira = get_object_or_404(Carteira, pk=cod_carteira)
        carteira.delete()
        return HttpResponse(status=204)
    except:
        return HttpResponse(status=404)

#################Ocorrência##########################

@api_view()
def lista_ocorrencia(request):
    busca = request.GET.get('buscar')
    querystring = request.META['QUERY_STRING']
    querydict = QueryDict(querystring).dict()
    buscar = querydict.get('buscar')
    ordenar = querydict.get('ordenar')
    urlx = request.GET.get("ordenar")
    if busca:
        lista_registros = (Ocorrencia.objects.filter(num_ocorrencia__icontains=busca) |
                        Ocorrencia.objects.filter(desc_ocorrencia__icontains=busca))
        dados = {'registros': lista_registros, 'buscar': buscar}
        if ordenar:
            lista_registros = (Ocorrencia.objects.filter(num_ocorrencia__icontains=busca).order_by(ordenar) |
                               Ocorrencia.objects.filter(desc_ocorrencia__icontains=busca).order_by(ordenar))
            dados = {'registros': lista_registros, 'buscar': buscar, 'ordenar': ordenar}
    elif ordenar:
        lista_registros = Ocorrencia.objects.order_by(ordenar)
        dados = {'registros': lista_registros, 'ordenar': ordenar}
    else:
        lista_registros = Ocorrencia.objects.all()
        dados = {'registros': lista_registros}

    ''' PK '''
    if dados['registros']:
        registro = dados['registros'][0]
        dados['pk'] = registro._meta.db_returning_fields[0].name
        dados['columns'] = [x.name for x in registro._meta.get_fields() if x.concrete]

    ''' URL '''
    dados['urlx'] = urlx
    dados['registros'] = [{col: get_values(registro, col) for col in dados['columns']} for registro in dados['registros']]
    return JsonResponse(dados)


@api_view()
def delete_ocorrencia(request, num_ocorrencia):
    try:
        ocorrencia = get_object_or_404(Ocorrencia, pk=num_ocorrencia)
        ocorrencia.delete()
        return HttpResponse(status=204)
    except:
        return HttpResponse(status=404)

