from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.http import HttpResponse
from .models import DiscadorOcorrencia, Sistema
from django.http import QueryDict

def index(request):
    return render(request, 'index.html')


def sist_novo(request):
    return render(request, 'sist_novo.html')


def forms(request):
    sistema = Sistema.objects.all()
    dados2 = {'sistema': sistema}
    return render(request, 'forms.html', dados2)


def processa_sist(request):
    if request.method == "POST":
        nome_sistema = request.POST.get('nome_sistema')
        val_sist_novo = Sistema.objects.filter(nome_sistema__icontains=nome_sistema)
        if len(val_sist_novo) > 0:
            return HttpResponse('Nome de sistema já cadastrado')
        else:
            sistema = Sistema(nome_sistema=nome_sistema)
            sistema.save()
            return redirect('/forms')
    else:
        return HttpResponse('Erro interno')


def processa_formulario(request):
    if request.method == "POST":
        carteira = request.POST.get('carteira')
        ocorrencia = request.POST.get('ocorrencia')
        alo = request.POST.get('alo')
        cpc = request.POST.get('cpc')

        sist = Sistema.objects.get(codigo=request.POST.get('sist'))

        discador = DiscadorOcorrencia(sist=sist,
                                      carteira=carteira,
                                      ocorrencia=ocorrencia,
                                      alo=alo,
                                      cpc=cpc)
        discador.save()
        return redirect('/buscar')
    else:
        return HttpResponse('Erro interno')


def deletar(request, id):
    registro = get_object_or_404(DiscadorOcorrencia, pk=id)
    registro.delete()
    return redirect('buscar')


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

    elif ordenar:
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



def lista_sist(request):
    lista_sistemas = Sistema.objects.all()
    dados1 = {'sistemas': lista_sistemas}
    return render(request, 'lista_sist.html', dados1)

