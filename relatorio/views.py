from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import DiscadorOcorrencia


def index(request):
    return render(request, 'index.html')


def forms(request):
    return render(request, 'forms.html')


def processa_formulario(request):
    if request.method == "POST":
        sistema = request.POST.get('sistema')
        carteira = request.POST.get('carteira')
        ocorrencia = request.POST.get('ocorrencia')
        alo = request.POST.get('alo')
        cpc = request.POST.get('cpc')
        discador = DiscadorOcorrencia(sistema=sistema,
                                      carteira=carteira,
                                      ocorrencia=ocorrencia,
                                      alo=alo,
                                      cpc=cpc,)
        discador.save()
        return redirect('/listagem/')
    else:
        return HttpResponse('Erro interno')


def listagem (request):
    registros = DiscadorOcorrencia.objects.all()

    dados = {'registros': registros}

    busca = request.GET.get('search')
    if busca:
        registros = DiscadorOcorrencia.objects.filter(carteita__icontains=busca)

    return render(request, 'listagem.html', dados)


def deletar(request, id):
    registro = get_object_or_404(DiscadorOcorrencia, pk=id)
    registro.delete()
    return redirect('/listagem/')



def buscar(request):
    lista_registros = DiscadorOcorrencia.objects.all()

    busca = request.GET.get('buscar')
    if busca:
        lista_registros = DiscadorOcorrencia.objects.filter(sistema__icontains=busca)

    dados = {
        'registros': lista_registros
    }

    return render(request, 'buscar.html', dados)
