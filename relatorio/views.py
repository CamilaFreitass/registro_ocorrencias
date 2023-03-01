from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import DiscadorOcorrencia, Sistema
from django.http import QueryDict

def index(request):
    return render(request, 'index.html')


def forms(request):
    sistema = Sistema.objects.all()
    dados2 = {'sistema': sistema}
    return render(request, 'forms.html', dados2)


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
    print(urlx)
    if busca:
        lista_registros = (DiscadorOcorrencia.objects.filter(carteira__icontains=busca) |
                            DiscadorOcorrencia.objects.filter(ocorrencia__icontains=busca) |
                          DiscadorOcorrencia.objects.filter(sist_icontains=busca))
        dados = {'registros': lista_registros, 'buscar': buscar}
        if ordenar:
            lista_registros = (DiscadorOcorrencia.objects.filter(carteira__icontains=busca).order_by(ordenar) |
                                DiscadorOcorrencia.objects.filter(ocorrencia__icontains=busca).order_by(ordenar) |
                               Sistema.objects.filter(nome_sistema_icontains=busca))
            dados = {'registros': lista_registros, 'buscar': buscar, 'ordenar': ordenar}
    elif ordenar:
        lista_registros = DiscadorOcorrencia.objects.order_by(ordenar)
        dados = {'registros': lista_registros, 'ordenar': ordenar}
    else:
        lista_registros = DiscadorOcorrencia.objects.all()
        dados = {'registros': lista_registros}
    dados['urlx'] = urlx
    return render(request, 'listagem.html', dados)





