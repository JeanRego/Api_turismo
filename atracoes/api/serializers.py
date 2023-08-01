from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao

class AtracaoSerializer(ModelSerializer):
    
    class Meta:
        model = Atracao
        fields = ('id','nome','descricao','horario_funcionamento','foto','idade_minima')
        
        def __str__(self):
            return self.nome