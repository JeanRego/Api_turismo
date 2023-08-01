from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from endereco.api.serializers import EnderecoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer

class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True, read_only=True)
    endereco = EnderecoSerializer(read_only=True)
    comentario = ComentarioSerializer(many=True, read_only=True)
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    
    class Meta:
        model = PontoTuristico
        fields = ['id','nome','foto', 'descricao','aprovado','atracoes','comentario','avaliacoes','endereco','foto']