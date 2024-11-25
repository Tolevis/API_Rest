from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Item
from .serializers import ItemSerializer
from rest_framework.authentication import TokenAuthentication

# Endpoint para criar um item
class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# Endpoint para listar todos os itens
class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# Endpoint para consultar um item individual
class ItemDetailView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
# Endpoint para atualizar um item
class ItemUpdateView(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
