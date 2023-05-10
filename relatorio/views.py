from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import DiscadorOcorrencia, Sistema, Carteira, Ocorrencia
import requests
from .forms import OcorrenciaForms, SistemaForms, CarteiraForms, DiscadorOcorrenciaForms

def index(request):
    return render(request, 'index.html')



def lista_classificacao(request):
    url = 'http://127.0.0.1:8000/api/lista_classificacao'
    params = request.GET.dict()
    response = requests.get(url, params=params)
    data = response.json()
    return render(request, 'listagem.html', data)


def delete_classificacao(request, id):
    url = f'http://127.0.0.1:8000/api/delete_classificacao/{id}'
    params = request.GET.dict()
    response = requests.get(url, params=params)
    if response.status_code == 204:
        print('Classificação deletado com sucesso')
    else:
        print(f'Erro ao deletar classificação')
    return redirect('lista_classificacao')


def classificacao_nova(request):
    form = DiscadorOcorrenciaForms()
    if request.method == 'POST':
        form = DiscadorOcorrenciaForms(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'classificacao_nova.html', {'form': form})


def create_classificacao(request):
    if request.method == 'POST':
        dados_do_formulario = request.POST

        response = requests.post('http://127.0.0.1:8000/api/create_classificacao/', data=dados_do_formulario)

        if response.status_code == 201:
            return redirect('lista_classificacao')
        elif response.status_code == 409:
            return HttpResponse('Essa classificação já existe')
        else:
            return HttpResponse('Erro no POST')

    else:
        return HttpResponse('Não é POST!')


def update_classificacao(request, id):
    classificacao = get_object_or_404(DiscadorOcorrencia, id=id)
    form = DiscadorOcorrenciaForms(instance=classificacao)
    if request.method == 'POST':

        data = request.POST.dict()
        del data['csrfmiddlewaretoken']

        response = requests.put(f'http://127.0.0.1:8000/api/update_classificacao/{id}/', data=data)

        if response.status_code == 200:
            return redirect('lista_classificacao')
        else:
            return HttpResponse('Ocorrência inválida!')
    elif request.method == 'GET':
        return render(request, 'classificacao_nova.html', {'form': form, 'classificacao': classificacao})




##############SISTEMA###################



def lista_sistema(request):
    url = f'http://127.0.0.1:8000/api/lista_sistema'
    params = request.GET.dict()
    response = requests.get(url, params=params)
    data = response.json()
    return render(request, 'listagem.html', data)


def delete_sistema(request, codigo):
    url = f'http://127.0.0.1:8000/api/delete_sistema/{codigo}'
    params = request.GET.dict()
    response = requests.get(url, params=params)
    if response.status_code == 204:
        print('Sistema deletado com sucesso')
    else:
        print(f'Erro ao deletar sistema')
    return redirect('lista_sistema')


def sistema_novo(request):
    form = SistemaForms()
    if request.method == 'POST':
        form = SistemaForms(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'sistema_novo.html', {'form': form})


def create_sistema(request):
    if request.method == 'POST':
        dados_do_formulário = {
        'nome_sistema': request.POST['nome_sistema']
        }

        response = requests.post('http://127.0.0.1:8000/api/create_sistema/', data=dados_do_formulário)

        if response.status_code == 201:
            return redirect('lista_sistema')
        elif response.status_code == 409:
            return HttpResponse('Sistema já existe')
        else:
            return HttpResponse('Erro no POST')

    else:
        return HttpResponse('Não é POST!')


def update_sistema(request, codigo):
    sistema = get_object_or_404(Sistema, codigo=codigo)
    form = SistemaForms(instance=sistema)
    if request.method == 'POST':

        data = request.POST.dict()
        del data['csrfmiddlewaretoken']

        response = requests.put(f'http://127.0.0.1:8000/api/update_sistema/{codigo}/', data=data)

        if response.status_code == 200:
            return redirect('lista_sistema')
        else:
            return HttpResponse('Sistema inválido!')
    elif request.method == 'GET':
        return render(request, 'sistema_novo.html', {'form': form, 'sistema': sistema})


##############CARTEIRA###################


def lista_carteira(request):
    url = 'http://127.0.0.1:8000/api/lista_carteira'
    params = request.GET.dict()
    response = requests.get(url, params=params)
    data = response.json()
    return render(request, 'listagem.html', data)


def carteira_nova(request):
    form = CarteiraForms()
    if request.method == 'POST':
        form = CarteiraForms(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'carteira_nova.html', {'form': form})


def delete_carteira(request, cod_carteira):
    url = f'http://127.0.0.1:8000/api/delete_carteira/{cod_carteira}'
    params = request.GET.dict()
    response = requests.get(url, params=params)
    if response.status_code == 204:
        print('Carteira deletada com sucesso')
    else:
        print(f'Erro ao deletar carteira')
    return redirect('lista_carteira')


def create_carteira(request):
    if request.method == 'POST':
        dados_do_formulário = {
        'nome_carteira': request.POST['nome_carteira']
        }

        response = requests.post('http://127.0.0.1:8000/api/create_carteira/', data=dados_do_formulário)

        if response.status_code == 201:
            return redirect('lista_carteira')
        elif response.status_code == 409:
            return HttpResponse('Carteira já existe')
        else:
            return HttpResponse('Erro no POST')

    else:
        return HttpResponse('Não é POST!')


def update_carteira(request, cod_carteira):
    carteira = get_object_or_404(Carteira, cod_carteira=cod_carteira)
    form = CarteiraForms(instance=carteira)
    if request.method == 'POST':

        data = request.POST.dict()
        del data['csrfmiddlewaretoken']

        response = requests.put(f'http://127.0.0.1:8000/api/update_carteira/{cod_carteira}/', data=data)

        if response.status_code == 200:
            return redirect('lista_carteira')
        else:
            return HttpResponse('Carteira inválida!')
    elif request.method == 'GET':
        return render(request, 'carteira_nova.html', {'form': form, 'carteira': carteira})


##############OCORRÊNCIA###################

def lista_ocorrencia(request):
    url = 'http://127.0.0.1:8000/api/lista_ocorrencia'
    params = request.GET.dict()
    response = requests.get(url, params=params)
    data = response.json()
    return render(request, 'listagem.html', data)


def ocorrencia_nova(request):
    form = OcorrenciaForms()
    if request.method == 'POST':
        form = OcorrenciaForms(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'ocorrencia_nova.html', {'form': form})


def delete_ocorrencia(request, pk_interna):
    url = f'http://127.0.0.1:8000/api/delete_ocorrencia/{pk_interna}'
    params = request.GET.dict()
    response = requests.get(url, params=params)
    if response.status_code == 204:
        print('Item deletado com sucesso')
    else:
        print(f'Erro ao deletar item')
    return redirect('lista_ocorrencia')


def create_ocorrencia(request):
    if request.method == 'POST':
        dados_do_formulário = {
        'num_ocorrencia': request.POST['num_ocorrencia'],
        'desc_ocorrencia': request.POST['desc_ocorrencia']
        }

        response = requests.post('http://127.0.0.1:8000/api/create_ocorrencia/', data=dados_do_formulário)

        if response.status_code == 201:
            return redirect('lista_ocorrencia')
        elif response.status_code == 409:
            return HttpResponse('Número de ocorrência ou descrição já existe')
        else:
            return HttpResponse('Erro no POST')

    else:
        return HttpResponse('Não é POST!')



def update_ocorrencia(request, pk_interna):
    ocorrencia = get_object_or_404(Ocorrencia, pk_interna=pk_interna)
    form = OcorrenciaForms(instance=ocorrencia)
    if request.method == 'POST':

        data = request.POST.dict()
        del data['csrfmiddlewaretoken']

        response = requests.put(f'http://127.0.0.1:8000/api/update_ocorrencia/{pk_interna}/', data=data)

        if response.status_code == 200:
            return redirect('lista_ocorrencia')
        else:
            return HttpResponse('Ocorrência inválida!')
    elif request.method == 'GET':
        return render(request, 'ocorrencia_nova.html', {'form': form, 'ocorrencia': ocorrencia})




