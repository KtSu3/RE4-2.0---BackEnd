from django.urls import path, include
from rest_framework import status
from rest_framework.routers import DefaultRouter
from .views import LoginAPI, user_view, CadastrarAtendimento, ListViabilidadeView, ListTecnicoView, CadastrarViabilidade,  EquipamentoSListView, ListAssuntosViewSet, ListVendedoresViewSet, ListTecnicoViewSet, ListAssuntosViewSet, ListTecnicoViewSet, LoginView,  ListVendedoresViewSet,  ListFabricanteViewSet, ListModeloViewSet, ListConclusaoTesteViewSet, ListProdutoViewSet, CadastrarEquipamentos, create_tecnico, create_assunto, create_vendedor, criar_fabricante, criar_conclusao_teste, criar_modelo, criar_produto

#EndPoints
#ListViewSets---------------------------------------------------#
router = DefaultRouter()
router.register(r'list_fabricantes', ListFabricanteViewSet)
router.register(r'list_conclusao', ListConclusaoTesteViewSet )
router.register(r'list_produtos', ListProdutoViewSet )
router.register(r'list_modelo', ListModeloViewSet )
router.register(r'list_assunto', ListAssuntosViewSet )
router.register(r'list_vendedor', ListVendedoresViewSet )
router.register(r'list_tecnico', ListTecnicoViewSet )
#---------------------------------------------------------------#

#EndPoints------------------------------------------------------#
urlpatterns = [
    path('', include(router.urls)),
    #Login
    path('login/', LoginAPI.as_view(), name='api-login'),
    path('user/', user_view, name='user-api'),
    path('loginn/', LoginView.as_view(), name='loginn'),
    #Stock
    path('criar_fabricantes/', criar_fabricante, name='criar_fabricante'),  
    path('criar_conclusao_teste/', criar_conclusao_teste, name='criar_conclusao_teste'),
    path('criar_modelo/', criar_modelo, name='criar_modelo'),
    path('criar_produto/', criar_produto, name='criar_produto'),
    path('register_equipment/', CadastrarEquipamentos.as_view(), name='register_equipment'),
    path('list_equipamentos/', EquipamentoSListView.as_view(), name='list_equipamentos'),
    #Project
    path('create_vendedor/', create_vendedor, name='create_vendedor'), 
    path('create_assunto/',  create_assunto, name='create_assunto'),
    path('create_tecnico/', create_tecnico, name='create_assunto'),
    path('listtecnico/', create_tecnico, name=''),
    path('register_atendimento/', CadastrarAtendimento.as_view(), name='register_atendimento'),
    path('register_viabilidade/', CadastrarViabilidade.as_view(), name='register_viabilidade'),
    path('list_viabilidades/', ListViabilidadeView.as_view(), name='list_viabilidades'),
    path('list_tecnicoo/', ListTecnicoView.as_view(), name='list_tecnico'),
    
]
