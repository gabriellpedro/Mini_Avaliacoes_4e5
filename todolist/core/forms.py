from .models import TaskModel
from django.forms import ModelForm

class TaskForm(ModelForm):
    class Meta:
        model = TaskModel
        fields = ['nome_atividade','data_atividade']
        error_messages = {
        'nome_atividade': {
            'required': ("Informe o nome da atividade."),
        },
        'data_atividade':{
            'required': ("Informe a data do atividade"),
        }
    }

    def clean_nome(self):
        nome_atividade = self.cleaned_data['nome_atividade']
        return nome_atividade.upper()
    
    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data