from .models import TaskModel
from django.forms import ModelForm

class TaskForm(ModelForm):
    class Meta:
        model = TaskModel
        fields = ['nome_atividade','dia_atividade','mes_atividade']
        error_messages = {
        'nome_atividade': {
            'required': ("Informe o nome do feriado."),
        },
        'dia_atividade': {
            'required': ("Informe o dia do feriado."),
        },
        'mes_atividade': {
            'required': ("Informe o mês do feriado."),
        }
    }

    def clean_nome(self):
        nome_atividade = self.cleaned_data['nome_atividade']
        return nome_atividade.upper()
    
    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data