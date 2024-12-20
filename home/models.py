from django.db import models

class Doador(models.Model):
    nome = models.CharField(max_length=50)
    cpf_cnpj = models.CharField(max_length=14)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=15)  # Aceita números e formatação de telefone
    cep = models.CharField(max_length=8)  # Somente números do CEP
    perfil_doacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class CriadorCampanha(models.Model):
    nome = models.CharField(max_length=50)
    username = models.CharField(max_length=50, default="N/C")
    cnpj = models.CharField(max_length=14)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=15)
    cidade = models.CharField(max_length=30, default="N/C")
    cep = models.CharField(max_length=8)
    perfil_campanha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14, unique=True)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=15)
    cidade = models.CharField(max_length=30, default="N/C")
    cep = models.CharField(max_length=8, default=000)
    endereco = models.CharField(max_length=100)
    perfil_campanha = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} ({self.cnpj})"

class Campanha(models.Model):
    criador = models.ForeignKey(CriadorCampanha, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    perfil_doacao = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    estabelecimentos = models.ManyToManyField(Estabelecimento)
    descricao = models.TextField(max_length=400)

    def __str__(self):
        return self.nome