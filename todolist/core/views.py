from datetime import datetime
from django.shortcuts import redirect, render
from core.forms import TaskForm
from core.models import TaskModel


def cadastro(request):
    if request.method == 'POST':
        form_atividade = TaskForm(request.POST)
        if form_atividade.is_valid():
            TaskModel.objects.create(**form_atividade.cleaned_data)
            return redirect('/')
        else:
            contexto = {
                'form_atividade': form_atividade
            }
            return render (request, 'cadastro.html', contexto)
    else:
        contexto = {
            'form_atividade': TaskForm()
        }
        return render (request, 'cadastro.html', contexto)
    
def verifica_atividade(request): 
    data_atividade = datetime.now().date()
    qs = TaskModel.objects.all()
    verifica_data = qs.filter(
            data_atividade__year=data_atividade.year,
            data_atividade__month=data_atividade.month,
            data_atividade__day=data_atividade.day
    )
    nome_default = list()
    if len(verifica_data) > 0:
        for atividade in verifica_data:
            insercao = {
                "nome_atividade" : atividade.nome_atividade,
                "data_atividade": atividade.data_atividade,
            }
            nome_default.append(insercao)
        return render(request, 'index.html', {"nome_default": nome_default})
    return render(request, 'index.html', {"nome_default": [{"nome_atividade" : "Não há atividades para hoje."}]})    
    