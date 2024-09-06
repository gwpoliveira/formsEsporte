from django.contrib import admin
from .models import FormularioEsporte
from .models import Atividade


class FormularioEsporteAdmin(admin.ModelAdmin):
    # Campos que aparecerão na lista de visualização
    list_display = ('nome', 'nivel', 'serie', 'idade', 'unidade', 'responsavel', 'telefone')

    # Campos que poderão ser pesquisados
    search_fields = ('nome', 'responsavel', 'telefone')

    # Filtros laterais para facilitar a busca
    list_filter = ('unidade', 'serie', 'nivel')


# Registro do modelo de formulário de esporte
admin.site.register(FormularioEsporte, FormularioEsporteAdmin)
admin.site.register(Atividade)
