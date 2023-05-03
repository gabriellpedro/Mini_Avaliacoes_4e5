from django.contrib import admin
from datetime import date

from core.models import TaskModel

class AtividadeModelAdmin(admin.ModelAdmin):
    list_display = ('nome_atividade','dia_atividade','mes_atividade','modificado_em','registrado_esse_ano')
    date_hierarchy = 'modificado_em'
    search_fields = ('nome_atividade','dia_atividade', 'mes_atividade')
    list_filter = ('modificado_em',)

    def registrado_esse_ano(self, obj):
        hoje = date.today()
        return obj.modificado_em.year == hoje.year
    
    registrado_esse_ano.short_description = "Resgistrado esse ano"
    registrado_esse_ano.boolean = True


admin.site.register(TaskModel,AtividadeModelAdmin)
