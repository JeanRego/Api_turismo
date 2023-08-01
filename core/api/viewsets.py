from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class PontoturisticoViewSet(ModelViewSet):
    filterset_fields = {'nome':['icontains'],'descricao':['icontains']} #icontains me permite pesquisar independente das letras ser maiusculas ou minusculas
    serializer_class = PontoTuristicoSerializer
    permission_classes = [IsAuthenticated]
    #authentication_classes = [TokenAuthentication]

   #*****************************************************
   #*********  SOBRESCREVENDO METODOS CRUD *************** 
   #*****************************************************
    
    def get_queryset(self): #FILTRO
        return PontoTuristico.objects.filter(aprovado=True)
    
    def list(self,request,*args,**kwargs): #LISTAR
        return super(PontoturisticoViewSet,self).list(request,*args,**kwargs)
        
    def create(self, request, *args, **kwargs): #POST
        #return Response({'Hello': request.data['nome']})
        return super(PontoturisticoViewSet,self).create(request,*args,**kwargs)
    
    def destroy(self, request, *args, **kwargs): #DELETE
        return super(PontoturisticoViewSet,self).destroy(request,*args,**kwargs)
    
    def retrieve(self, request, *args, **kwargs): #VALIDAÇÔES. TAMBEM DISPARA NO GET POREM
                                                  #SÒ RETORNA O QUE FOR VALIDADO DE ACORDO COM O QUE EU QUISER 
        return super(PontoturisticoViewSet,self).retrieve(request,*args,**kwargs)
        
    def update(self, request, *args, **kwargs): #ATUALIZAR
        return super(PontoturisticoViewSet,self).update(request,*args,**kwargs)
    
    def partial_update(self, request, *args, **kwargs): #ATUALIZAR PARCIALMENTE UM OBJETO
        return super(PontoturisticoViewSet,self).partial_update(request,*args,**kwargs)       
    
    #****************************************************#
    #****************************************************#
    #****************************************************#
    
    @action(methods=['get','post'], detail=True)
    def denunciar(self,request, pk=None):
        return Response({'OK'})
    
    @action(methods=['get'], detail=False)
    def teste(self,request):
        pass
    
    