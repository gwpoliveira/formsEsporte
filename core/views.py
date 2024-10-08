from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FormularioEsporte
from .forms import FormularioEsporteForm
import pandas as pd
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def lista_inscritos(request):
    inscritos_list = FormularioEsporte.objects.all()  # Obtém todos os inscritos
    paginator = Paginator(inscritos_list, 30)  # Pagina com 10 inscritos por página

    page = request.GET.get('page')  # Obtém o número da página
    try:
        inscritos = paginator.page(page)
    except PageNotAnInteger:
        inscritos = paginator.page(1)  # Se a página não for um inteiro, mostra a primeira página
    except EmptyPage:
        inscritos = paginator.page(paginator.num_pages)  # Se a página estiver fora do intervalo, mostra a última página

    return render(request, 'inscritos.html', {'inscritos': inscritos})


def home(request):
    if request.method == 'POST':
        form = FormularioEsporteForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o formulário
            return redirect('success')  # Redireciona para a página de sucesso
    else:
        form = FormularioEsporteForm()

    return render(request, 'home.html', {'form': form})


@login_required
def exportar_inscritos_excel(request):
    # Obtenha todos os inscritos e selecione os campos necessários
    inscritos = FormularioEsporte.objects.all()

    # Crie uma lista para armazenar os dados
    inscritos_dados = []

    # Itere sobre os inscritos para coletar os dados
    for inscrito in inscritos:
        # Coleta as atividades associadas ao inscrito e transforma em uma string
        atividades = ', '.join([atividade.nome for atividade in inscrito.atividades.all()])

        # Adiciona os dados do inscrito, incluindo as atividades, à lista
        inscritos_dados.append({
            'nome': inscrito.nome,
            'nivel': inscrito.nivel,
            'serie': inscrito.serie,
            'idade': inscrito.idade,
            'unidade': inscrito.unidade,
            'responsavel': inscrito.responsavel,
            'telefone': inscrito.telefone,
            'atividades': atividades,  # Inclui as atividades
        })

    # Cria um DataFrame com os dados dos inscritos
    df = pd.DataFrame(inscritos_dados)

    # Define a resposta HTTP com o tipo de arquivo Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="inscritos_esporte.xlsx"'

    # Gera o arquivo Excel
    df.to_excel(response, index=False)

    return response

def success_view(request):
    return render(request, 'success.html')


