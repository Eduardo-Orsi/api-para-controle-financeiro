from django.contrib import admin
from django.urls import path
from Finanças.views import DespesaAPIView, ReceitaAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/receitas/', ReceitaAPIView.as_view()),
    path('api/receitas/<str:pk>', ReceitaAPIView.as_view()),
    path('api/receitas/<str:pk>/', ReceitaAPIView.as_view()),
    path('api/despesas/', DespesaAPIView.as_view()),
    path('api/despesas/<str:pk>', DespesaAPIView.as_view()),
    path('api/despesas/<str:pk>/', DespesaAPIView.as_view())
]
