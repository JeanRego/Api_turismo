from rest_framework.serializers import ModelSerializer
from endereco.models import Endereco

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id','linha1','linha2']
        
        def __str__(self):
            return self.linha1