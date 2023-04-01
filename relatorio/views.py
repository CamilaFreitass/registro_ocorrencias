from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.http import HttpResponse
from .models import DiscadorOcorrencia, Sistema, Carteira, Ocorrencia
from django.http import QueryDict


def index(request):
    return render(request, 'index.html')


def forms(request):
    sistema = Sistema.objects.all()
    carteira = Carteira.objects.all()
    ocorrencia = Ocorrencia.objects.all()
    dados2 = {'sistema': sistema, 'carteira': carteira, 'ocorrencia': ocorrencia}
    return render(request, 'forms.html', dados2)

def buscar(request):
    busca = request.GET.get('buscar')
    querystring = request.META['QUERY_STRING']
    querydict = QueryDict(querystring).dict()
    buscar = querydict.get('buscar')
    ordenar = querydict.get('ordenar')
    urlx = request.GET.get("ordenar")
    if busca:
        lista_registros = (DiscadorOcorrencia.objects.filter(sist__nome_sistema__icontains=busca) |
                            DiscadorOcorrencia.objects.filter(carteira__icontains=busca) |
                            DiscadorOcorrencia.objects.filter(ocorrencia__icontains=busca))
        dados = {'registros': lista_registros, 'buscar': buscar}

        if ordenar:
            lista_registros = (DiscadorOcorrencia.objects.filter(sist__nome_sistema__icontains=busca) |
                                DiscadorOcorrencia.objects.filter(carteira__icontains=busca).order_by(ordenar) |
                                DiscadorOcorrencia.objects.filter(ocorrencia__icontains=busca).order_by(ordenar))

            dados = {'registros': lista_registros, 'buscar': buscar, 'ordenar': ordenar}
    elif ordenar:
        lista_registros = DiscadorOcorrencia.objects.order_by(ordenar)
        dados = {'registros': lista_registros, 'ordenar': ordenar}
    else:
        lista_registros = DiscadorOcorrencia.objects.all()
        dados = {'registros': lista_registros}
    dados['urlx'] = urlx
    return render(request, 'listagem.html', dados)


def processa_formulario(request):
    if request.method == "POST":
        alo = request.POST.get('alo')
        cpc = request.POST.get('cpc')
        promessa = request.POST.get('cpc')

        sist = Sistema.objects.get(codigo=request.POST.get('sist'))

        carteira = Carteira.objects.get(cod_carteira=request.POST.get('carteira'))

        ocorrencia = Ocorrencia.objects.get(num_ocorrencia=request.POST.get('ocorrencia'))

        disc_ocorrencia = DiscadorOcorrencia.objects.filter(sist=sist, carteira=carteira, ocorrencia=ocorrencia)
        if len(disc_ocorrencia) > 0:
            return HttpResponse('Objeto já cadastrado no sistema!')
        else:

            discador = DiscadorOcorrencia(sist=sist,
                                      carteira=carteira,
                                      ocorrencia=ocorrencia,
                                      alo=alo,
                                      cpc=cpc,
                                      promessa=promessa)
            discador.save()
            return redirect('/buscar')
    else:
        return HttpResponse('Erro interno')

def deletar(request, id):
    registro = get_object_or_404(DiscadorOcorrencia, pk=id)
    registro.delete()
    return redirect('buscar')

##############SISTEMA###################

def lista_sist(request):
    lista_sistemas = Sistema.objects.all()
    dados1 = {'sistemas': lista_sistemas}
    return render(request, 'lista_sist.html', dados1)


def sist_novo(request):
    return render(request, 'sist_novo.html')


def processa_sist(request):
    if request.method == "POST":
        nome_sistema = request.POST.get('nome_sistema')
        val_sist_novo = Sistema.objects.filter(nome_sistema__icontains=nome_sistema)
        if len(val_sist_novo) > 0:
            return HttpResponse('Nome de sistema já cadastrado')
        else:
            sistema = Sistema(nome_sistema=nome_sistema)
            sistema.save()
            return redirect('lista_sist')
    else:
        return HttpResponse('Erro interno')


def update_sist(request, codigo):
    sist = get_object_or_404(Sistema, pk=codigo)
    sists = {"sist": sist}
    return render(request, 'update_sist.html', sists)


def editar_sist(request, codigo):
    nome_sistema = request.POST.get("nome_sistema")
    sist = Sistema.objects.get(pk=codigo)
    sist.nome_sistema = nome_sistema
    sist.save()
    return redirect('/lista_sist')


def deletar_sist(request, codigo):
    sist = get_object_or_404(Sistema, pk=codigo)
    sist.delete()
    return redirect('/lista_sist')

##############CARTEIRA###################


def lista_carteira(request):
    lista_carteiras = Carteira.objects.all()
    dados2 = {'carteiras': lista_carteiras}
    return render(request, 'lista_carteira.html', dados2)

def carteira_nova(request):
    return render(request, 'carteira_nova.html')

def processa_carteira(request):
    if request.method == "POST":
        nome_carteira = request.POST.get('nome_carteira')
        val_carteira_nova = Carteira.objects.filter(nome_carteira__icontains=nome_carteira)
        if len(val_carteira_nova) > 0:
            return HttpResponse('Nome da carteira já cadastrado')
        else:
            carteira = Carteira(nome_carteira=nome_carteira)
            carteira.save()
            return redirect('lista_carteira')
    else:
        return HttpResponse('Erro interno')

def deletar_carteira(request, cod_carteira):
    cart = get_object_or_404(Carteira, pk=cod_carteira)
    cart.delete()
    return redirect('lista_carteira')

def update_carteira(request, cod_carteira):
    carteira = get_object_or_404(Carteira, pk=cod_carteira)
    carteiras = {"carteira": carteira}
    return render(request, 'update_carteira.html', carteiras)


def editar_carteira(request, cod_carteira):
    nome_carteira = request.POST.get("nome_carteira")
    carteira = Carteira.objects.get(pk=cod_carteira)
    carteira.nome_carteira = nome_carteira
    carteira.save()
    return redirect('lista_carteira')

##############OCORRÊNCIA###################

def lista_ocorrencia(request):
    lista_ocorrencia = Ocorrencia.objects.all()
    dados3 = {'ocorrencias': lista_ocorrencia}
    return render(request, 'lista_ocorrencia.html', dados3)

def ocorrencia_nova(request):
    return render(request, 'ocorrencia_nova.html')

def processa_ocorrencia(request):
    if request.method == "POST":
        num_ocorrencia = request.POST.get('num_ocorrencia')
        desc_ocorrencia = request.POST.get('desc_ocorrencia')
        val_num_ocorrencia = Ocorrencia.objects.filter(num_ocorrencia__icontains=num_ocorrencia)
        val_desc_ocorrencia = Ocorrencia.objects.filter(desc_ocorrencia__icontains=desc_ocorrencia)
        if len(val_num_ocorrencia) > 0 or len(val_desc_ocorrencia) > 0:
            return HttpResponse('Número ou descrição da ocorrência já cadastrado')
        else:
            ocorrencia = Ocorrencia(num_ocorrencia=num_ocorrencia, desc_ocorrencia=desc_ocorrencia)
            ocorrencia.save()
            return redirect('lista_ocorrencia')
    else:
        return HttpResponse('Erro interno')
