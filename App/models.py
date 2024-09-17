from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser
from dirtyfields import DirtyFieldsMixin 
#------------------------------------#Projeto------------------------------------------------#

class Campo1(models.TextChoices):
    SIM = 'S'
    NAO = 'N'
    
class Status(models.TextChoices):
    CADASTRADO = 'C', 'Cadastrado'
    EMTESTE = 'ET', 'Em Teste'
    TESTADO = 'T', 'Testado'
    DESCARTE = 'D', 'Descarte'
    RMA = 'RMA', 'RMA'
    RETESTADO = 'RE', 'Retestado'
    EMCAMPO = 'EC', 'Campo'

class Vendedores(models.Model):
    vendedor = models.CharField(max_length=100, unique=True)
    # date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.vendedor}"
    
class Tecnicos(models.Model):
    tecnico = models.CharField(max_length=100, unique=True)
    # date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.tecnico}"

class Assuntos(models.Model):
    assunto = models.CharField(max_length=100, unique=True)
    # date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.assunto}"

class CadastroViabilidade(models.Model):
    projeto_responsavel = models.CharField(max_length=100)
    vendedor_responsavel = models.ForeignKey(Vendedores, on_delete=models.CASCADE)
    viavel = models.CharField(max_length=100)  # Corrigido de 'vivavel' para 'viavel'
    descricao_projeto = models.TextField()
    descricao_comercial = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return (f"{self.projeto_responsavel} - {self.vendedor_responsavel} - {self.viavel} - "
                f"{self.descricao_projeto} - {self.descricao_comercial} - {self.date}")


class CadastroTecnicos(models.Model):
    projeto_responsavel = models.CharField(max_length=100)
    tecnico_responsavel = models.ForeignKey(Tecnicos, on_delete=models.CASCADE)
    assunto = models.ForeignKey(Assuntos, on_delete=models.CASCADE)
    info_atendimento = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return (f"{self.projeto_responsavel} - {self.tecnico_responsavel} - {self.info_atendimento} - "
                f"{self.assunto} - {self.date}")

#------------------------------------#Stock------------------------------------------------#

class Fabricantes(models.Model):
    fabricantes = models.CharField(max_length=100, unique=True)
    date = models.DateField(auto_now=True)

class Modelos(models.Model):
    modelos = models.CharField(max_length=100, unique=True)
    date = models.DateField(auto_now=True)

class Produtos(models.Model):
    produtos = models.CharField(max_length=100, unique=True)
    date = models.DateField(auto_now=True)

class ConclusaoTeste(models.Model):
    conclusao_teste = models.CharField(max_length=100, unique=True) 
    date = models.DateField(auto_now=True)

class Equipamentos(models.Model):
    produtos = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelos, on_delete=models.CASCADE)
    fabricante = models.ForeignKey(Fabricantes, on_delete=models.CASCADE)
    conclusao_teste = models.ForeignKey(ConclusaoTeste, on_delete=models.CASCADE)
    numero_serie = models.CharField(max_length=100)
    observacao = models.TextField()
    username = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)

class Movimentacoes(models.Model):
    equipamento = models.ForeignKey(Equipamentos, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=3,
        choices=Status.choices,
        default=Status.CADASTRADO
    )
    observacao = models.TextField() 
    date = models.DateField(auto_now=True)


#Autentication ---

class User(AbstractBaseUser, DirtyFieldsMixin):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    grup = models.IntegerField()
    login = models.DateField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        if not self.pk or 'password' in self.get_dirty_fields():
            self.password = make_password(self.password)
        super().save(*args, **kwargs)