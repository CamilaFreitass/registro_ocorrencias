from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from relatorio.models import DiscadorOcorrencia, Sistema, Carteira, Ocorrencia
from django.http import QueryDict
from rest_framework.decorators import api_view
from django.http import JsonResponse
from relatorio.templatetags.extras import get_values
from relatorio.forms import OcorrenciaForms, SistemaForms, CarteiraForms, DiscadorOcorrenciaForms
from django.core.paginator import Paginator

#################Geral##########################

@api_view()
def lista_classificacao(request):
    busca = request.GET.get('buscar')
    querystring = request.META['QUERY_STRING']
    querydict = QueryDict(querystring).dict()
    buscar = querydict.get('buscar')
    ordenar = querydict.get('ordenar')
    urlx = request.GET.get("ordenar")
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '2')
    if not (parametro_limit.isdigit() and int(parametro_limit) > 0):
        parametro_limit = '2'
    if busca:
        lista_registros = (DiscadorOcorrencia.objects.filter(sist__nome_sistema__icontains=busca) |
                            DiscadorOcorrencia.objects.filter(carteira__nome_carteira__icontains=busca) |
                            DiscadorOcorrencia.objects.filter(ocorrencia__num_ocorrencia__icontains=busca))
        registros_paginator = Paginator(lista_registros, parametro_limit)
        nu_pages = registros_paginator.num_pages
        lista = list(range(1, nu_pages + 1))
        pagina_atual = registros_paginator.get_page(parametro_page)
        num_pagina_atual = pagina_atual.number
        tem_prox_pagina = pagina_atual.has_next()
        num_prox_pagina = pagina_atual.next_page_number() if tem_prox_pagina else None
        tem_page_anterior = pagina_atual.has_previous()
        num_page_anterior = pagina_atual.previous_page_number() if tem_page_anterior else None
        dados = {'registros': pagina_atual, 'buscar': buscar,
                 'tem_page_anterior': tem_page_anterior, 'num_page_anterior': num_page_anterior,
                 'nu_pages': nu_pages, 'num_pagina_atual': num_pagina_atual,
                 'tem_prox_pagina': tem_prox_pagina, 'num_prox_pagina': num_prox_pagina,
                 'lista': lista}


        if ordenar:
            lista_registros = (DiscadorOcorrencia.objects.filter(sist__nome_sistema__icontains=busca) |
                                DiscadorOcorrencia.objects.filter(carteira__nome_carteira__icontains=busca).order_by(ordenar) |
                                DiscadorOcorrencia.objects.filter(ocorrencia__num_ocorrencia__icontains=busca).order_by(ordenar))
            registros_paginator = Paginator(lista_registros, parametro_limit)
            nu_pages = registros_paginator.num_pages
            lista = list(range(1, nu_pages + 1))
            pagina_atual = registros_paginator.get_page(parametro_page)
            num_pagina_atual = pagina_atual.number
            tem_prox_pagina = pagina_atual.has_next()
            num_prox_pagina = pagina_atual.next_page_number() if tem_prox_pagina else None
            tem_page_anterior = pagina_atual.has_previous()
            num_page_anterior = pagina_atual.previous_page_number() if tem_page_anterior else None
            dados = {'registros': pagina_atual, 'buscar': buscar, 'ordenar': ordenar,
                     'tem_page_anterior': tem_page_anterior, 'num_page_anterior': num_page_anterior,
                     'nu_pages': nu_pages, 'num_pagina_atual': num_pagina_atual,
                     'tem_prox_pagina': tem_prox_pagina, 'num_prox_pagina': num_prox_pagina,
                     'lista': lista}
    elif ordenar:
        lista_registros = DiscadorOcorrencia.objects.order_by(ordenar)
        registros_paginator = Paginator(lista_registros, parametro_limit)
        nu_pages = registros_paginator.num_pages
        lista = list(range(1, nu_pages + 1))
        pagina_atual = registros_paginator.get_page(parametro_page)
        num_pagina_atual = pagina_atual.number
        tem_prox_pagina = pagina_atual.has_next()
        num_prox_pagina = pagina_atual.next_page_number() if tem_prox_pagina else None
        tem_page_anterior = pagina_atual.has_previous()
        num_page_anterior = pagina_atual.previous_page_number() if tem_page_anterior else None
        dados = {'registros': pagina_atual, 'ordenar': ordenar,
                 'tem_page_anterior': tem_page_anterior, 'num_page_anterior': num_page_anterior,
                 'nu_pages': nu_pages, 'num_pagina_atual': num_pagina_atual,
                 'tem_prox_pagina': tem_prox_pagina, 'num_prox_pagina': num_prox_pagina,
                 'lista': lista}
    else:
        lista_registros = DiscadorOcorrencia.objects.all()
        registros_paginator = Paginator(lista_registros, parametro_limit)
        nu_pages = registros_paginator.num_pages
        lista = list(range(1, nu_pages + 1))
        try:
            pagina_atual = registros_paginator.get_page(parametro_page)
        except:
            pagina_atual = registros_paginator.get_page(1)
        num_pagina_atual = pagina_atual.number
        tem_prox_pagina = pagina_atual.has_next()
        num_prox_pagina = pagina_atual.next_page_number() if tem_prox_pagina else None
        tem_page_anterior = pagina_atual.has_previous()
        num_page_anterior = pagina_atual.previous_page_number() if tem_page_anterior else None
        dados = {'registros': pagina_atual,'tem_page_anterior': tem_page_anterior,
                 'num_page_anterior': num_page_anterior, 'nu_pages': nu_pages,
                 'num_pagina_atual': num_pagina_atual, 'tem_prox_pagina': tem_prox_pagina,
                 'num_prox_pagina': num_prox_pagina, 'lista': lista}

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


@api_view(['POST'])
def create_classificacao(request):
    form = DiscadorOcorrenciaForms(request.data)
    if form.is_valid():
        sist = form.cleaned_data['sist']
        carteira = form.cleaned_data['carteira']
        ocorrencia = form.cleaned_data['ocorrencia']
        classificacao_existe = DiscadorOcorrencia.objects.filter(sist=sist,
                                                         carteira=carteira,
                                                         ocorrencia=ocorrencia)
        if classificacao_existe:
            return HttpResponse(status=409)
        else:
            classificacao = DiscadorOcorrencia(sist=form.cleaned_data['sist'],
                                    carteira=form.cleaned_data['carteira'],
                                    ocorrencia=form.cleaned_data['ocorrencia'],
                                    alo=form.cleaned_data['alo'],
                                    cpc=form.cleaned_data['cpc'],
                                    promessa=form.cleaned_data['promessa'],)
            classificacao.save()
            return HttpResponse(status=201)


@api_view(['PUT'])
def update_classificacao(request, id):
    classificacao = DiscadorOcorrencia.objects.get(id=id)
    if request.method == 'PUT':
        form = DiscadorOcorrenciaForms(request.data, instance=classificacao)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=400)


#################Sistema##########################

@api_view()
def lista_sistema(request):
    busca = request.GET.get('buscar')
    querystring = request.META['QUERY_STRING']
    querydict = QueryDict(querystring).dict()
    buscar = querydict.get('buscar')
    ordenar = querydict.get('ordenar')
    urlx = request.GET.get('ordenar')
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '2')
    if not (parametro_limit.isdigit() and int(parametro_limit) > 0):
        parametro_limit = '2'
    if busca:
        lista_registros = (Sistema.objects.filter(codigo__icontains=busca) |
                        Sistema.objects.filter(nome_sistema__icontains=busca))
        registros_paginator = Paginator(lista_registros, parametro_limit)
        nu_pages = registros_paginator.num_pages
        lista = list(range(1, nu_pages + 1))
        pagina_atual = registros_paginator.get_page(parametro_page)
        num_pagina_atual = pagina_atual.number
        tem_prox_pagina = pagina_atual.has_next()
        num_prox_pagina = pagina_atual.next_page_number() if tem_prox_pagina else None
        tem_page_anterior = pagina_atual.has_previous()
        num_page_anterior = pagina_atual.previous_page_number() if tem_page_anterior else None
        dados = {'registros': pagina_atual, 'buscar': buscar,
                 'tem_page_anterior': tem_page_anterior, 'num_page_anterior': num_page_anterior,
                 'nu_pages': nu_pages, 'num_pagina_atual': num_pagina_atual,
                 'tem_prox_pagina': tem_prox_pagina, 'num_prox_pagina': num_prox_pagina,
                 'lista': lista}
        if ordenar:
            lista_registros = (Sistema.objects.filter(codigo__icontains=busca).order_by(ordenar) |
                               Sistema.objects.filter(nome_sistema__icontains=busca).order_by(ordenar))
            registros_paginator = Paginator(lista_registros, parametro_limit)
            nu_pages = registros_paginator.num_pages
            lista = list(range(1, nu_pages + 1))
            pagina_atual = registros_paginator.get_page(parametro_page)
            num_pagina_atual = pagina_atual.number
            tem_prox_pagina = pagina_atual.has_next()
            num_prox_pagina = pagina_atual.next_page_number() if tem_prox_pagina else None
            tem_page_anterior = pagina_atual.has_previous()
            num_page_anterior = pagina_atual.previous_page_number() if tem_page_anterior else None
            dados = {'registros': pagina_atual, 'buscar': buscar, 'ordenar': ordenar,
                     'tem_page_anterior': tem_page_anterior, 'num_page_anterior': num_page_anterior,
                     'nu_pages': nu_pages, 'num_pagina_atual': num_pagina_atual,
                     'tem_prox_pagina': tem_prox_pagina, 'num_prox_pagina': num_prox_pagina,
                     'lista': lista}
    elif ordenar:
        lista_registros = Sistema.objects.order_by(ordenar)
        registros_paginator = Paginator(lista_registros, parametro_limit)
        nu_pages = registros_paginator.num_pages
        lista = list(range(1, nu_pages + 1))
        pagina_atual = registros_paginator.get_page(parametro_page)
        num_pagina_atual = pagina_atual.number
        tem_prox_pagina = pagina_atual.has_next()
        num_prox_pagina = pagina_atual.next_page_number() if tem_prox_pagina else None
        tem_page_anterior = pagina_atual.has_previous()
        num_page_anterior = pagina_atual.previous_page_number() if tem_page_anterior else None
        dados = {'registros': pagina_atual, 'ordenar': ordenar,
                 'tem_page_anterior': tem_page_anterior, 'num_page_anterior': num_page_anterior,
                 'nu_pages': nu_pages, 'num_pagina_atual': num_pagina_atual,
                 'tem_prox_pagina': tem_prox_pagina, 'num_prox_pagina': num_prox_pagina,
                 'lista': lista}
    else:
        lista_registros = Sistema.objects.all()
        registros_paginator = Paginator(lista_registros, parametro_limit)
        nu_pages = registros_paginator.num_pages
        lista = list(range(1, nu_pages + 1))
        try:
            pagina_atual = registros_paginator.get_page(parametro_page)
        except:
            pagina_atual = registros_paginator.get_page(1)
        num_pagina_atual = pagina_atual.number
        tem_prox_pagina = pagina_atual.has_next()
        num_prox_pagina = pagina_atual.next_page_number() if tem_prox_pagina else None
        tem_page_anterior = pagina_atual.has_previous()
        num_page_anterior = pagina_atual.previous_page_number() if tem_page_anterior else None
        dados = {'registros': pagina_atual,'tem_page_anterior': tem_page_anterior,
                 'num_page_anterior': num_page_anterior, 'nu_pages': nu_pages,
                 'num_pagina_atual': num_pagina_atual, 'tem_prox_pagina': tem_prox_pagina,
                 'num_prox_pagina': num_prox_pagina, 'lista': lista}

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


@api_view(['POST'])
def create_sistema(request):
    form = SistemaForms(request.data)
    if form.is_valid():
        sistema = Sistema(nome_sistema=form.cleaned_data['nome_sistema'])
        sistema.save()
        return HttpResponse(status=201)
    else:
        return HttpResponse(status=409)

@api_view(['PUT'])
def update_sistema(request, codigo):
    sistema = Sistema.objects.get(codigo=codigo)
    if request.method == 'PUT':
        form = SistemaForms(request.data, instance=sistema)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=400)



#################Carteira##########################

@api_view()
def lista_carteira(request):
    busca = request.GET.get('buscar')
    querystring = request.META['QUERY_STRING']
    querydict = QueryDict(querystring).dict()
    buscar = querydict.get('buscar')
    ordenar = querydict.get('ordenar')
    urlx = request.GET.get("ordenar")
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '2')
    if not (parametro_limit.isdigit() and int(parametro_limit) > 0):
        parametro_limit = '2'
    if busca:
        lista_registros = (Carteira.objects.filter(cod_carteira__icontains=busca) |
                        Carteira.objects.filter(nome_carteira__icontains=busca))
        registros_paginator = Paginator(lista_registros, parametro_limit)
        nu_pages = registros_paginator.num_pages
        lista = list(range(1, nu_pages + 1))
        pagina_atual = registros_paginator.get_page(parametro_page)
        num_pagina_atual = pagina_atual.number
        tem_prox_pagina = pagina_atual.has_next()
        num_prox_pagina = pagina_atual.next_page_number() if tem_prox_pagina else None
        tem_page_anterior = pagina_atual.has_previous()
        num_page_anterior = pagina_atual.previous_page_number() if tem_page_anterior else None
        dados = {'registros': pagina_atual, 'buscar': buscar,
                 'tem_page_anterior': tem_page_anterior, 'num_page_anterior': num_page_anterior,
                 'nu_pages': nu_pages, 'num_pagina_atual': num_pagina_atual,
                 'tem_prox_pagina': tem_prox_pagina, 'num_prox_pagina': num_prox_pagina,
                 'lista': lista}
        if ordenar:
            lista_registros = (Carteira.objects.filter(cod_carteira__icontains=busca).order_by(ordenar) |
                               Carteira.objects.filter(nome_carteira__icontains=busca).order_by(ordenar))
            registros_paginator = Paginator(lista_registros, parametro_limit)
            nu_pages = registros_paginator.num_pages
            lista = list(range(1, nu_pages + 1))
            pagina_atual = registros_paginator.get_page(parametro_page)
            num_pagina_atual = pagina_atual.number
            tem_prox_pagina = pagina_atual.has_next()
            num_prox_pagina = pagina_atual.next_page_number() if tem_prox_pagina else None
            tem_page_anterior = pagina_atual.has_previous()
            num_page_anterior = pagina_atual.previous_page_number() if tem_page_anterior else None
            dados = {'registros': pagina_atual, 'buscar': buscar, 'ordenar': ordenar,
                     'tem_page_anterior': tem_page_anterior, 'num_page_anterior': num_page_anterior,
                     'nu_pages': nu_pages, 'num_pagina_atual': num_pagina_atual,
                     'tem_prox_pagina': tem_prox_pagina, 'num_prox_pagina': num_prox_pagina,
                     'lista': lista}
    elif ordenar:
        lista_registros = Carteira.objects.order_by(ordenar)
        registros_paginator = Paginator(lista_registros, parametro_limit)
        nu_pages = registros_paginator.num_pages
        lista = list(range(1, nu_pages + 1))
        pagina_atual = registros_paginator.get_page(parametro_page)
        num_pagina_atual = pagina_atual.number
        tem_prox_pagina = pagina_atual.has_next()
        num_prox_pagina = pagina_atual.next_page_number() if tem_prox_pagina else None
        tem_page_anterior = pagina_atual.has_previous()
        num_page_anterior = pagina_atual.previous_page_number() if tem_page_anterior else None
        dados = {'registros': pagina_atual, 'ordenar': ordenar,
                 'tem_page_anterior': tem_page_anterior, 'num_page_anterior': num_page_anterior,
                 'nu_pages': nu_pages, 'num_pagina_atual': num_pagina_atual,
                 'tem_prox_pagina': tem_prox_pagina, 'num_prox_pagina': num_prox_pagina,
                 'lista': lista}
    else:
        lista_registros = Carteira.objects.all()
        registros_paginator = Paginator(lista_registros, parametro_limit)
        nu_pages = registros_paginator.num_pages
        lista = list(range(1, nu_pages + 1))
        try:
            pagina_atual = registros_paginator.get_page(parametro_page)
        except:
            pagina_atual = registros_paginator.get_page(1)
        num_pagina_atual = pagina_atual.number
        tem_prox_pagina = pagina_atual.has_next()
        num_prox_pagina = pagina_atual.next_page_number() if tem_prox_pagina else None
        tem_page_anterior = pagina_atual.has_previous()
        num_page_anterior = pagina_atual.previous_page_number() if tem_page_anterior else None
        dados = {'registros': pagina_atual, 'tem_page_anterior': tem_page_anterior,
                 'num_page_anterior': num_page_anterior, 'nu_pages': nu_pages,
                 'num_pagina_atual': num_pagina_atual, 'tem_prox_pagina': tem_prox_pagina,
                 'num_prox_pagina': num_prox_pagina, 'lista': lista}

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


@api_view(['POST'])
def create_carteira(request):
    form = CarteiraForms(request.data)
    if form.is_valid():
        campo_unico = form.cleaned_data['nome_carteira']
        numero_existe = Carteira.objects.filter(nome_carteira=campo_unico)
        if numero_existe:
            return HttpResponse(status=409)
        else:
            carteira = Carteira(nome_carteira=form.cleaned_data['nome_carteira'])
            carteira.save()
            return HttpResponse(status=201)


@api_view(['PUT'])
def update_carteira(request, cod_carteira):
    carteira = Carteira.objects.get(cod_carteira=cod_carteira)
    if request.method == 'PUT':
        form = CarteiraForms(request.data, instance=carteira)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=400)


#################Ocorrência##########################

@api_view()
def lista_ocorrencia(request):
    busca = request.GET.get('buscar')
    querystring = request.META['QUERY_STRING']
    querydict = QueryDict(querystring).dict()
    buscar = querydict.get('buscar')
    ordenar = querydict.get('ordenar')
    urlx = request.GET.get("ordenar")
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '2')
    if not (parametro_limit.isdigit() and int(parametro_limit) > 0):
        parametro_limit = '2'
    if busca:
        lista_registros = (Ocorrencia.objects.filter(num_ocorrencia__icontains=busca) |
                        Ocorrencia.objects.filter(desc_ocorrencia__icontains=busca))
        registros_paginator = Paginator(lista_registros, parametro_limit)
        nu_pages = registros_paginator.num_pages
        lista = list(range(1, nu_pages + 1))
        pagina_atual = registros_paginator.get_page(parametro_page)
        num_pagina_atual = pagina_atual.number
        tem_prox_pagina = pagina_atual.has_next()
        num_prox_pagina = pagina_atual.next_page_number() if tem_prox_pagina else None
        tem_page_anterior = pagina_atual.has_previous()
        num_page_anterior = pagina_atual.previous_page_number() if tem_page_anterior else None
        dados = {'registros': pagina_atual, 'buscar': buscar,
                 'tem_page_anterior': tem_page_anterior, 'num_page_anterior': num_page_anterior,
                 'nu_pages': nu_pages, 'num_pagina_atual': num_pagina_atual,
                 'tem_prox_pagina': tem_prox_pagina, 'num_prox_pagina': num_prox_pagina,
                 'lista': lista}
        if ordenar:
            lista_registros = (Ocorrencia.objects.filter(num_ocorrencia__icontains=busca).order_by(ordenar) |
                               Ocorrencia.objects.filter(desc_ocorrencia__icontains=busca).order_by(ordenar))
            registros_paginator = Paginator(lista_registros, parametro_limit)
            nu_pages = registros_paginator.num_pages
            lista = list(range(1, nu_pages + 1))
            pagina_atual = registros_paginator.get_page(parametro_page)
            num_pagina_atual = pagina_atual.number
            tem_prox_pagina = pagina_atual.has_next()
            num_prox_pagina = pagina_atual.next_page_number() if tem_prox_pagina else None
            tem_page_anterior = pagina_atual.has_previous()
            num_page_anterior = pagina_atual.previous_page_number() if tem_page_anterior else None
            dados = {'registros': pagina_atual, 'buscar': buscar, 'ordenar': ordenar,
                     'tem_page_anterior': tem_page_anterior, 'num_page_anterior': num_page_anterior,
                     'nu_pages': nu_pages, 'num_pagina_atual': num_pagina_atual,
                     'tem_prox_pagina': tem_prox_pagina, 'num_prox_pagina': num_prox_pagina,
                     'lista': lista}
    elif ordenar:
        lista_registros = Ocorrencia.objects.order_by(ordenar)
        registros_paginator = Paginator(lista_registros, parametro_limit)
        nu_pages = registros_paginator.num_pages
        lista = list(range(1, nu_pages + 1))
        pagina_atual = registros_paginator.get_page(parametro_page)
        num_pagina_atual = pagina_atual.number
        tem_prox_pagina = pagina_atual.has_next()
        num_prox_pagina = pagina_atual.next_page_number() if tem_prox_pagina else None
        tem_page_anterior = pagina_atual.has_previous()
        num_page_anterior = pagina_atual.previous_page_number() if tem_page_anterior else None
        dados = {'registros': pagina_atual, 'ordenar': ordenar,
                 'tem_page_anterior': tem_page_anterior, 'num_page_anterior': num_page_anterior,
                 'nu_pages': nu_pages, 'num_pagina_atual': num_pagina_atual,
                 'tem_prox_pagina': tem_prox_pagina, 'num_prox_pagina': num_prox_pagina,
                 'lista': lista}
    else:
        lista_registros = Ocorrencia.objects.all()
        registros_paginator = Paginator(lista_registros, parametro_limit)
        nu_pages = registros_paginator.num_pages
        lista = list(range(1, nu_pages + 1))
        try:
            pagina_atual = registros_paginator.get_page(parametro_page)
        except:
            pagina_atual = registros_paginator.get_page(1)
        num_pagina_atual = pagina_atual.number
        tem_prox_pagina = pagina_atual.has_next()
        num_prox_pagina = pagina_atual.next_page_number() if tem_prox_pagina else None
        tem_page_anterior = pagina_atual.has_previous()
        num_page_anterior = pagina_atual.previous_page_number() if tem_page_anterior else None
        dados = {'registros': pagina_atual, 'tem_page_anterior': tem_page_anterior,
                 'num_page_anterior': num_page_anterior, 'nu_pages': nu_pages,
                 'num_pagina_atual': num_pagina_atual, 'tem_prox_pagina': tem_prox_pagina,
                 'num_prox_pagina': num_prox_pagina, 'lista': lista}

    ''' PK '''
    if dados['registros']:
        registro = dados['registros'][0]
        dados['pk'] = registro._meta.pk.name  # registro._meta.db_returning_fields[0].name
        dados['columns'] = [x.name for x in registro._meta.get_fields() if x.concrete]

    ''' URL '''
    dados['urlx'] = urlx
    dados['registros'] = [{col: get_values(registro, col) for col in dados['columns']} for registro in dados['registros']]
    return JsonResponse(dados)


@api_view()
def delete_ocorrencia(request, pk_interna):
    try:
        ocorrencia = get_object_or_404(Ocorrencia, pk=pk_interna)
        ocorrencia.delete()
        return HttpResponse(status=204)
    except:
        return HttpResponse(status=404)

@api_view(['POST'])
def create_ocorrencia(request):
    form = OcorrenciaForms(request.data)
    if form.is_valid():
        campo_unico = form.cleaned_data['num_ocorrencia']
        numero_existe = Ocorrencia.objects.filter(num_ocorrencia=campo_unico)
        campo_unico1 = form.cleaned_data['desc_ocorrencia']
        descricao_existe = Ocorrencia.objects.filter(desc_ocorrencia=campo_unico1)
        if numero_existe or descricao_existe:
            return HttpResponse(status=409)
        else:
            ocorrencia = Ocorrencia(num_ocorrencia=form.cleaned_data['num_ocorrencia'],
                                    desc_ocorrencia=form.cleaned_data['desc_ocorrencia'])
            ocorrencia.save()
            return HttpResponse(status=201)


@api_view(['PUT'])
def update_ocorrencia(request, pk_interna):
    ocorrencia = Ocorrencia.objects.get(pk_interna=pk_interna)
    if request.method == 'PUT':
        form = OcorrenciaForms(request.data, instance=ocorrencia)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=400)