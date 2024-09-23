from rest_framework import serializers  
from .models import CadastroViabilidade, User, CadastroTecnicos, Modelos, Fabricantes, Produtos, ConclusaoTeste, Equipamentos, Vendedores, Assuntos, Tecnicos

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


#Project ---

class TecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnicos
        fields = ['id','tecnico']

class AssunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assuntos
        fields = ['id','assunto']

class VendTesteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedores
        fields = ['id','vendedor']


class TecnicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnicos
        fields = ['id', 'tecnico']

    def __init__(self, *args, **kwargs):
        super(TecnicosSerializer, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            print(f"Field: {field_name}, Value: {field}")


class AssuntosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assuntos
        fields = ['id', 'assunto']

    def __init__(self, *args, **kwargs):
        super(AssuntosSerializer, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            print(f"Field: {field_name}, Value: {field}")

class VendedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedores
        fields = ['id', 'vendedor']

    def __init__(self, *args, **kwargs):
        super(VendedoresSerializer, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            print(f"Field: {field_name}, Value: {field}")


class CadastroTecnicosSerializer(serializers.ModelSerializer):
    tecnico_responsavel_id = serializers.PrimaryKeyRelatedField(
        queryset=Tecnicos.objects.all(),
        source='tecnico_responsavel' 
    )
    assunto_id = serializers.PrimaryKeyRelatedField(
        queryset=Assuntos.objects.all(),
        source='assunto'
    )

    class Meta:
        model = CadastroTecnicos
        fields = ['projeto_responsavel', 'tecnico_responsavel_id', 'assunto_id', 'info_atendimento']

#----------------------------------Estoque----------------------------------#

class EquipamentoSerialier(serializers.ModelSerializer):
    produtos_id = serializers.PrimaryKeyRelatedField(
        queryset=Produtos.objects.all(),
        source='produtos'
    )
    conclusao_teste_id = serializers.PrimaryKeyRelatedField(
        queryset=ConclusaoTeste.objects.all(),
        source='conclusao_teste'
    )
    fabricante_id = serializers.PrimaryKeyRelatedField(
        queryset=Fabricantes.objects.all(),
        source='fabricante'
    )
    modelo_id = serializers.PrimaryKeyRelatedField(
        queryset=Modelos.objects.all(),
        source='modelo'
    )
    class Meta: 
        model = Equipamentos
        fields = ['numero_serie', 'observacao', 'conclusao_teste_id', 'fabricante_id', 'modelo_id', 'produtos_id' ]

    def create(self, validated_data):
        return super().create(validated_data)
    
class CadastroViabilidadeSerializer(serializers.ModelSerializer):
    vendedor_responsavel_id = serializers.PrimaryKeyRelatedField(
        queryset=Vendedores.objects.all(),
        source='vendedor_responsavel'
    )

    class Meta:
        model = CadastroViabilidade
        fields = ['projeto_responsavel', 'viavel', 'vendedor_responsavel_id', 'descricao_comercial', 'descricao_projeto']

    def create(self, validated_data):
        return CadastroViabilidade.objects.create(**validated_data)

class ViabilidadeListSerializer(serializers.ModelSerializer):
    vendedor_responsavel = serializers.StringRelatedField()

    class Meta:
        model = CadastroViabilidade
        fields = ['projeto_responsavel', 'vendedor_responsavel', 'viavel', 'descricao_projeto', 'descricao_comercial', 'date']

class TecnicoListSerializer(serializers.ModelSerializer):
    tecnico_responsavel = serializers.StringRelatedField()
    assunto = serializers.StringRelatedField()
    class Meta:
        model = CadastroTecnicos
        fields = ['projeto_responsavel', 'tecnico_responsavel', 'assunto', 'info_atendimento', 'date']


    
class ListFabricante(serializers.ModelSerializer):
    class Meta:
        model = Fabricantes
        fields = ['id','fabricantes']
class ListModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelos
        fields = ['id', 'modelos']

class ListProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = ['id', 'produtos']
class ListConclusaoTesteModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConclusaoTeste
        fields = ['id','conclusao_teste']

class FabricanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabricantes
        fields = ['id','fabricantes']

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelos
        fields = ['id','modelos']

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = ['id','produtos']

class ConclusaoTesteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConclusaoTeste
        fields = ['id','conclusao_teste']



class EquipamentosListSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    fabricante = FabricanteSerializer() 
    modelo = ModeloSerializer()          
    produtos = ProdutoSerializer()      
    conclusao_teste = ConclusaoTesteSerializer()  
    
    class Meta:
        model = Equipamentos
        fields = ['produtos', 'modelo', 'fabricante', 'conclusao_teste', 'numero_serie', 'observacao', 'date']
    def get_date(self, obj):
         return obj.date.strftime('%Y-%m-%d')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'grup', 'password']