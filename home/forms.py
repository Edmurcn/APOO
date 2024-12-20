from django import forms
from .models import Doador, CriadorCampanha, Estabelecimento, Campanha
from django_select2.forms import ModelSelect2MultipleWidget

class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        fields = '__all__'  # Inclui todos os campos do modelo

class CriadorCampanhaForm(forms.ModelForm):
    class Meta:
        model = CriadorCampanha
        fields = '__all__'

class EstabelecimentoForm(forms.ModelForm):
    class Meta:
        model = Estabelecimento
        fields = '__all__'


class CampanhaForm(forms.ModelForm):
    estabelecimentos = forms.ModelMultipleChoiceField(
        queryset=Estabelecimento.objects.none(),  # Inicialmente vazio
        widget=forms.CheckboxSelectMultiple,
        label="Estabelecimentos",
        required=False
    )

    def __init__(self, *args, criador=None, **kwargs):
        super().__init__(*args, **kwargs)
        if criador:
            # Filtra estabelecimentos pela cidade e perfil de doação
            self.fields['estabelecimentos'].queryset = Estabelecimento.objects.filter(
                cidade=criador.cidade,
                perfil_campanha=criador.perfil_campanha
            )

    class Meta:
        model = Campanha
        fields = ['nome', 'perfil_doacao', 'data_inicio', 'data_fim', 'estabelecimentos', 'descricao']

class LoginForm(forms.Form):
    username = forms.CharField(label="Nome de Usuário", max_length=50)
