from django.db import models
import uuid

class CategoriaReceita(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nome

class CategoriaDespesa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nome

class Receita(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descricao = models.CharField(max_length=100)
    valor = models.FloatField()
    data = models.DateField()
    categoria = models.ForeignKey(CategoriaReceita, on_delete=models.PROTECT, null=True, blank=True)
    
class Despesa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descricao = models.CharField(max_length=100)
    valor = models.FloatField()
    data = models.DateField()
    categoria = models.ForeignKey(CategoriaDespesa, on_delete=models.PROTECT, null=True, blank=True)
