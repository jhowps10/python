from django.forms import ModelForm
from app.models import Interacao

# Create the form class.
class InteracaoForm(ModelForm):
    class Meta:
        model = Interacao
        fields = ['data_contato', 'canal', 'contato', 'detalhes', 'ocasiao', 'data_evento', 'primeira_cor', 'segunda_cor', 'tamanho', 'locacao', 'motivo']