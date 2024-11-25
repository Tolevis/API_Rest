from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=100) # Nome do item
    descricao = models.TextField() # Descrição do item

    def __str__(self):
        return self.nome
