from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario

class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id','usuario','comentario','data','aprovado']
        
        def __str__(self):
            return self.usuario