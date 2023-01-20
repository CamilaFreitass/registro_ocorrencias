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
        return redirect('/buscar')
    else:
        return HttpResponse('Erro interno')


def deletar(request, id):
    registro = get_object_or_404(DiscadorOcorrencia, pk=id)
    registro.delete()
    return redirect('/listagem/')



def buscar(request):
    # pega o parametro "ordenar" e armazena na variável ordenar
    ordenar = request.GET.get('ordenar')

    # pega o parametro "buscar" e armazena na variável busca
    busca = request.GET.get('buscar')

    # confere se há alguma coisa na busca
    if busca:
        # se tiver algo na busca ele vai fazer um filtro para verificar se algum registro bate com o que foi passado
        lista_registros = DiscadorOcorrencia.objects.filter(sistema__icontains=busca)

    elif ordenar:
        lista_registros = DiscadorOcorrencia.objects.order_by('ocorrencia')

    else:
        # se não tiver nada na busca ele vai trazer tudo
        lista_registros = DiscadorOcorrencia.objects.all()

    dados = {
        'registros': lista_registros
    }

    return render(request, 'listagem.html', dados)


def listagem2(request):
    registros2 = DiscadorOcorrencia.objects.all()

    dados2 = {'registros2': registros2}

    return render(request, 'listagem2.html', dados2)




