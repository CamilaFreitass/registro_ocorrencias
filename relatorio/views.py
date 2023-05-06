from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import DiscadorOcorrencia, Sistema, Carteira, Ocorrencia
import requests
from .forms import OcorrenciaForms

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


def forms(request):
    sistema = Sistema.objects.all()
    carteira = Carteira.objects.all()
    ocorrencia = Ocorrencia.objects.all()
    dados2 = {'sistema': sistema, 'carteira': carteira, 'ocorrencia': ocorrencia}
    return render(request, 'forms.html', dados2)



def processa_formulario(request):
    if request.method == "POST":
        alo = request.POST.get('alo')
        cpc = request.POST.get('cpc')
        promessa = request.POST.get('promessa')

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
            return redirect('/lista_classificacao')
    else:
        return HttpResponse('Erro interno')





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
            return redirect('lista_sistema')
    else:
        return HttpResponse('Erro interno')


def update_sist(request, codigo):
    alistamento = get_object_or_404(Sistema, pk=codigo)
    alistamentos = {"sist": alistamento}
    return render(request, 'update_sist.html', alistamentos)


def editar_sist(request, codigo):
    nome_sistema = request.POST.get("nome_sistema")
    sist = Sistema.objects.get(pk=codigo)
    sist.nome_sistema = nome_sistema
    sist.save()
    return redirect('/lista_sist')


##############CARTEIRA###################


def lista_carteira(request):
    url = 'http://127.0.0.1:8000/api/lista_carteira'
    params = request.GET.dict()
    response = requests.get(url, params=params)
    data = response.json()
    return render(request, 'listagem.html', data)


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


def editar_carteira(request, cod_carteira):
    nome_carteira = request.POST.get("nome_carteira")
    carteira = Carteira.objects.get(pk=cod_carteira)
    carteira.nome_carteira = nome_carteira
    carteira.save()
    return redirect('lista_carteira')


def delete_carteira(request, cod_carteira):
    url = f'http://127.0.0.1:8000/api/delete_carteira/{cod_carteira}'
    params = request.GET.dict()
    response = requests.get(url, params=params)
    if response.status_code == 204:
        print('Carteira deletada com sucesso')
    else:
        print(f'Erro ao deletar carteira')
    return redirect('lista_carteira')


def update_carteira(request, cod_carteira):
    carteira = get_object_or_404(Carteira, pk=cod_carteira)
    carteiras = {"carteira": carteira}
    return render(request, 'carteira_nova.html', carteiras)


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


def delete_ocorrencia(request, num_ocorrencia):
    url = f'http://127.0.0.1:8000/api/delete_ocorrencia/{num_ocorrencia}'
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


# def update_ocorrencia(request, num_ocorrencia):
#     # busca a ocorrencia que queremos editar
#     ocorrencia = get_object_or_404(Ocorrencia, num_ocorrencia=num_ocorrencia)
#     # preenche o form com os dados da ocorrencia
#     form = OcorrenciaForms(instance=ocorrencia)
#     # se a requisição for 'POST' insere os registros alterados no banco de dados
#     if request.method == 'POST':
#         form = OcorrenciaForms(request.POST, instance=ocorrencia)
#         # verifica se o formulário está correto e depois validamos cada campo com cleaned_data
#         if form.is_valid():
#             ocorrencia = form.save(commit=False)
#             ocorrencia.num_ocorrencia = form.cleaned_data['num_ocorrencia']
#             ocorrencia.desc_ocorrencia = form.cleaned_data['desc_ocorrencia']
#             ocorrencia.save()
#             return redirect('lista_ocorrencia')
#         else:
#             return render(request, 'ocorrencia_nova.html', {'form': form, 'ocorrencia': ocorrencia})
#     # se a requisição for 'GET' visualiza o form preenchido
#     elif request.method == 'GET':
#         return render(request, 'ocorrencia_nova.html', {'form': form, 'ocorrencia': ocorrencia})


def update_ocorrencia(request, num_ocorrencia):
    ocorrencia = get_object_or_404(Ocorrencia, num_ocorrencia=num_ocorrencia)
    form = OcorrenciaForms(instance=ocorrencia)
    if request.method == 'POST':
        num_ocorrencia = request.POST['num_ocorrencia']
        desc_ocorrencia = request.POST['desc_ocorrencia']

        data = {'num_ocorrencia': num_ocorrencia,
                'desc_ocorrencia': desc_ocorrencia}

        response = requests.put(f'http://127.0.0.1:8000/api/update_ocorrencia/{num_ocorrencia}/', data=data)

        if response.status_code == 200:
            return redirect('lista_ocorrencia')
        else:
            return HttpResponse('Ocorrência inválida!')
    elif request.method == 'GET':
        return render(request, 'ocorrencia_nova.html', {'form': form, 'ocorrencia': ocorrencia})


