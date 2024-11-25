from rest_framework import serializers
from .models import Item
    
    #  Serializer para o modelo de Item. Converte os dados do Item em JSON e vice-versa.

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__' # Campos que serão incluídos na resposta JSON
