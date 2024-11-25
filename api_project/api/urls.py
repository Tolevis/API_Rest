from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('items/', views.ItemListView.as_view(), name='item-list'), # Lista todos os itens
    path('items/<int:pk>/', views.ItemDetailView.as_view(), name='item-detail'),
    path('items/create/', views.ItemCreateView.as_view(), name='item-create'), # Cria um novo item
    path('items/<int:pk>/update/', views.ItemUpdateView.as_view(), name='item-update'),
]
