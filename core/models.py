
from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from endereco.models import Endereco

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentario = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, default=1, null=True, blank=True)
    foto = models.ImageField(upload_to='imagens_pontos_turisticos', null=True, blank=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Ponto Turistico'
        verbose_name_plural = 'Pontos Turisticos'