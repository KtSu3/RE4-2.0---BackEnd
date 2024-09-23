from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import (LoginSerializer, CadastroViabilidadeSerializer, TecnicoListSerializer, ViabilidadeListSerializer, CadastroTecnicosSerializer, UserSerializer, TecSerializer, AssunSerializer, VendTesteSerializer, EquipamentosListSerializer, FabricanteSerializer, ConclusaoTesteSerializer, ModeloSerializer, ProdutoSerializer, ListFabricante, ListModeloSerializer,  ListProdutoSerializer, ListConclusaoTesteModeloSerializer, EquipamentoSerialier, TecnicosSerializer, AssuntosSerializer, VendedoresSerializer)
from .models import CadastroTecnicos, User, CadastroViabilidade, Fabricantes, Modelos, Produtos, ConclusaoTeste, Equipamentos, Assuntos, Tecnicos, Vendedores
from django.contrib.auth import authenticate, login as django_login
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.hashers import check_password, make_password
from django.views.decorators.csrf import csrf_exempt



class ListViabilidadeView(APIView):
    def get(self, request):
        viabilidades = CadastroViabilidade.objects.all()
        serializer = ViabilidadeListSerializer(viabilidades, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ListTecnicoView(APIView):
    def get(self, request):
        viabilidades = CadastroTecnicos.objects.all()
        serializer = TecnicoListSerializer(viabilidades, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Autenticate ---

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Email e senha são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Usuário não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        if not check_password(password, user.password):
            return Response({'error': 'Senha inválida.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['PUT','POST'])
def user_view(request):
    try:
        user = User.objects.get(email=request.data['email'])
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    




class LoginAPI(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                token, _ = Token.objects.get_or_create(user=user)
                django_login(request, user)
                return Response({'message': 'Login bem-sucedido.', 'token': token.key}, status=status.HTTP_200_OK)
            return Response({'error': 'Usuário ou senha incorretos.'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Project APIs ---
@api_view(['POST'])
def create_tecnico(request):
    serializer = TecnicosSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_assunto(request):
    serializer = AssuntosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_vendedor(request):
    serializer = VendedoresSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListTecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnicos.objects.all()
    serializer_class = TecSerializer

class ListVendedoresViewSet(viewsets.ModelViewSet):
    queryset = Vendedores.objects.all()
    serializer_class = VendTesteSerializer

class ListAssuntosViewSet(viewsets.ModelViewSet):
    queryset = Assuntos.objects.all()
    serializer_class = AssunSerializer



# Stock  APIs --- POST
class CadastrarEquipamentos(APIView):
    def post(self, request):
        serializer = EquipamentoSerialier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Equipamento cadastrado com Sucesso!'},
                            status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            print(Response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def criar_fabricante(request):
    serializer = FabricanteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def criar_modelo(request):
    serializer = ModeloSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def criar_produto(request):
    serializer = ProdutoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def criar_conclusao_teste(request):
    serializer = ConclusaoTesteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#GET ---
class ListFabricanteViewSet(viewsets.ModelViewSet):
    queryset = Fabricantes.objects.all()
    serializer_class = ListFabricante

class ListModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelos.objects.all()
    serializer_class = ListModeloSerializer

class ListProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ListProdutoSerializer

class ListConclusaoTesteViewSet(viewsets.ModelViewSet):
    queryset = ConclusaoTeste.objects.all()
    serializer_class = ListConclusaoTesteModeloSerializer

class EquipamentoSListView(APIView):
    def get(self, request):
        equipamentos = Equipamentos.objects.all()
        serializer = EquipamentosListSerializer(equipamentos, many=True)
        return Response(serializer.data)
    

#Create Atendimento ---
class CadastrarAtendimento(APIView):
    def post(self, request):
        serializer = CadastroTecnicosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Atendimento cadastrado com Sucesso!'}, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CadastrarViabilidade(APIView):
    def post(self, request):
        serializer = CadastroViabilidadeSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Atendimento cadastrado com Sucesso!'}, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




