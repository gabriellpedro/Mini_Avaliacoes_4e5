from django.db import models

class TaskModel(models.Model):
    nome_atividade = models.CharField('Atividade',max_length=50)
    data_atividade = models.DateField('Data da Atividade')
    modificado_em = models.DateTimeField(
        verbose_name= 'Modificado em', 
        auto_now_add=False, auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Atividades'
        verbose_name = 'Atividade'



    def __str__(self):
        return self.nome_atividade
