from django import forms
from .models import FormularioEsporte, Atividade

class FormularioEsporteForm(forms.ModelForm):
    class Meta:
        model = FormularioEsporte
        fields = ['nome', 'nivel', 'serie', 'idade', 'unidade', 'responsavel', 'telefone', 'atividades']

    def __init__(self, *args, **kwargs):
        super(FormularioEsporteForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['nivel'].widget.attrs.update({'class': 'form-control'})
        self.fields['serie'].widget.attrs.update({'class': 'form-control'})
        self.fields['idade'].widget.attrs.update({'class': 'form-control'})
        self.fields['unidade'].widget.attrs.update({'class': 'form-select'})
        self.fields['responsavel'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefone'].widget.attrs.update({'class': 'form-control'})
        self.fields['atividades'].widget = forms.CheckboxSelectMultiple()  # Adicionar o widget de seleção múltipla
        self.fields['atividades'].queryset = Atividade.objects.all()  # Definir as atividades disponíveis
