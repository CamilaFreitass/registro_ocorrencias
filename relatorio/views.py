from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import DiscadorOcorrencia, Sistema, Carteira, Ocorrencia
import requests
from .forms import OcorrenciaForms, SistemaForms, CarteiraForms, DiscadorOcorrenciaForms
from django.contrib import messages
from django.contrib.messages import constants
from decouple import config


def index(request):
    return render(request, 'index.html')



def lista_classificacao(request):
    url = 'http://localhost:80/api/lista_classificacao'
    params = request.GET.dict()
    response = requests.get(url, params=params)
    data = response.json()
    return render(request, 'listagem.html', data)


def delete_classificacao(request, id):
    url = f'http://localhost:80/api/delete_classificacao/{id}'
    params = request.GET.dict()
    response = requests.get(url, params=params)
    if response.status_code == 204:
        messages.add_message(request, constants.SUCCESS, 'Classificação deletada com sucesso')
    else:
        messages.add_message(request, constants.ERROR, 'Erro ao deletar classificação')
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

        response = requests.post('http://localhost:80/api/create_classificacao/', data=dados_do_formulario)

        if response.status_code == 201:
            messages.add_message(request, constants.SUCCESS, 'Classificação criada com sucesso.')
            return redirect('lista_classificacao')
        elif response.status_code == 409:
            messages.add_message(request, constants.ERROR, 'Essa classificação já existe.')
            return redirect('classificacao_nova')
        else:
            messages.add_message(request, constants.WARNING, 'Classificação inválida!')
            return redirect('classificacao_nova')
    else:
        messages.add_message(request, constants.WARNING, 'Erro interno!')
        return redirect('classificacao_nova')


def update_classificacao(request, id):
    classificacao = get_object_or_404(DiscadorOcorrencia, id=id)
    form = DiscadorOcorrenciaForms(instance=classificacao)
    if request.method == 'POST':

        data = request.POST.dict()
        del data['csrfmiddlewaretoken']

        response = requests.put(f'http://localhost:80/api/update_classificacao/{id}/', data=data)

        if response.status_code == 200:
            messages.add_message(request, constants.SUCCESS, 'Classificação atualizada com sucesso')
            return redirect('lista_classificacao')
        elif response.status_code == 409:
            messages.add_message(request, constants.ERROR, 'Essa classificação já existe')
            return redirect('lista_classificacao')
        else:
            messages.add_message(request, constants.WARNING, 'Classificação inválida')
            return redirect('lista_classificacao')
    elif request.method == 'GET':
        return render(request, 'classificacao_nova.html', {'form': form, 'classificacao': classificacao})




##############SISTEMA###################



def lista_sistema(request):
    url = f'http://localhost:80/api/lista_sistema'
    params = request.GET.dict()
    response = requests.get(url, params=params)
    data = response.json()
    return render(request, 'listagem.html', data)


def delete_sistema(request, codigo):
    url = f'http://localhost:80/api/delete_sistema/{codigo}'
    params = request.GET.dict()
    response = requests.get(url, params=params)
    if response.status_code == 204:
        messages.add_message(request, constants.SUCCESS, 'Sistema deletado com sucesso')
    else:
        messages.add_message(request, constants.ERROR, 'Erro ao deletar sistema')
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
        dados_do_formulario = request.POST

        response = requests.post('http://localhost:80/api/create_sistema/', data=dados_do_formulario)

        if response.status_code == 201:
            messages.add_message(request, constants.SUCCESS, 'Sistema criado com sucesso.')
            return redirect('lista_sistema')
        else:
            messages.add_message(request, constants.ERROR, 'Esse sistema já existe.')
            return redirect('sistema_novo')
    else:
        messages.add_message(request, constants.WARNING, 'Erro interno!')
        return redirect('sistema_novo')


def update_sistema(request, codigo):
    sistema = get_object_or_404(Sistema, codigo=codigo)
    form = SistemaForms(instance=sistema)
    if request.method == 'POST':

        data = request.POST.dict()
        del data['csrfmiddlewaretoken']

        response = requests.put(f'http://localhost:80/api/update_sistema/{codigo}/', data=data)

        if response.status_code == 200:
            messages.add_message(request, constants.SUCCESS, 'Sistema atualizado com sucesso')
            return redirect('lista_sistema')
        else:
            messages.add_message(request, constants.WARNING, 'Sistema inválido!')
            return redirect('lista_sistema')
    elif request.method == 'GET':
        return render(request, 'sistema_novo.html', {'form': form, 'sistema': sistema})


##############CARTEIRA###################


def lista_carteira(request):
    url = 'http://localhost:80/api/lista_carteira'
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
    url = f'http://localhost:80/api/delete_carteira/{cod_carteira}'
    params = request.GET.dict()
    response = requests.get(url, params=params)
    if response.status_code == 204:
        messages.add_message(request, constants.SUCCESS, 'Carteira deletada com sucesso')
    else:
        messages.add_message(request, constants.ERROR, 'Erro ao deletar carteira')
    return redirect('lista_carteira')


def create_carteira(request):
    if request.method == 'POST':
        dados_do_formulario = request.POST

        response = requests.post('http://localhost:80/api/create_carteira/', data=dados_do_formulario)

        if response.status_code == 201:
            messages.add_message(request, constants.SUCCESS, 'Carteira criada com sucesso.')
            return redirect('lista_carteira')
        else:
            messages.add_message(request, constants.ERROR, 'Essa carteira já existe.')
            return redirect('carteira_nova')
    else:
        messages.add_message(request, constants.WARNING, 'Erro interno!')
        return redirect('carteira_nova')


def update_carteira(request, cod_carteira):
    carteira = get_object_or_404(Carteira, cod_carteira=cod_carteira)
    form = CarteiraForms(instance=carteira)
    if request.method == 'POST':

        data = request.POST.dict()
        del data['csrfmiddlewaretoken']

        response = requests.put(f'http://localhost:80/api/update_carteira/{cod_carteira}/', data=data)

        if response.status_code == 200:
            messages.add_message(request, constants.SUCCESS, 'Carteira atualizada com sucesso')
            return redirect('lista_carteira')
        else:
            messages.add_message(request, constants.WARNING, 'Carteira inválida')
            return redirect('lista_carteira')
    elif request.method == 'GET':
        return render(request, 'carteira_nova.html', {'form': form, 'carteira': carteira})


##############OCORRÊNCIA###################

def lista_ocorrencia(request):
    url = 'http://localhost:80/api/lista_ocorrencia'
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
    url = f'http://localhost:80/api/delete_ocorrencia/{pk_interna}'
    params = request.GET.dict()
    response = requests.get(url, params=params)
    if response.status_code == 204:
        messages.add_message(request, constants.SUCCESS, 'Ocorrência deletada com sucesso')
    else:
        messages.add_message(request, constants.ERROR, 'Erro ao deletar ocorrência')
    return redirect('lista_ocorrencia')


def create_ocorrencia(request):
    if request.method == 'POST':
        dados_do_formulario = request.POST

        response = requests.post('http://localhost:80/api/create_ocorrencia/', data=dados_do_formulario)

        if response.status_code == 201:
            messages.add_message(request, constants.SUCCESS, 'Ocorrência criada com sucesso.')
            return redirect('lista_ocorrencia')
        else:
            messages.add_message(request, constants.ERROR, 'Essa ocorrência já existe.')
            return redirect('ocorrencia_nova')
    else:
        messages.add_message(request, constants.WARNING, 'Erro interno!')
        return redirect('ocorrencia_nova')



def update_ocorrencia(request, pk_interna):
    ocorrencia = get_object_or_404(Ocorrencia, pk_interna=pk_interna)
    form = OcorrenciaForms(instance=ocorrencia)
    if request.method == 'POST':

        data = request.POST.dict()
        del data['csrfmiddlewaretoken']

        response = requests.put(f'http://localhost:80/api/update_ocorrencia/{pk_interna}/', data=data)

        if response.status_code == 200:
            messages.add_message(request, constants.SUCCESS, 'Ocorrência atualizada com sucesso')
            return redirect('lista_ocorrencia')
        else:
            messages.add_message(request, constants.WARNING, 'Ocorrência inválida')
            return redirect('lista_ocorrencia')
    elif request.method == 'GET':
        return render(request, 'ocorrencia_nova.html', {'form': form, 'ocorrencia': ocorrencia})




