from rest_framework.response import Response
from rest_framework.views import APIView
from Finanças.models import Receita, Despesa
from Finanças.serializer import ReceitaSerializer, DespesaSerializer
from rest_framework import status

class ReceitaAPIView(APIView):
    """API's de Receitas"""

    def get(self, request, pk=None):
        if pk:
            queryset = Receita.objects.get(pk=pk)
            serializer_class = ReceitaSerializer(queryset)
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        else:
            queryset = Receita.objects.all()
            serializer_class = ReceitaSerializer(queryset, many=True)
            return Response(serializer_class.data, status=status.HTTP_200_OK)

    def post(self, request):
        queryset = ReceitaSerializer(data=request.data)
        queryset.is_valid(raise_exception=True)
        queryset.save()
        return Response(queryset.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None):
        if pk:
            if len(str(pk)) > 36 or len(str(pk)) < 36:
                return Response(data="ID inválido", status=status.HTTP_400_BAD_REQUEST)
            else:
                if Receita.objects.filter(pk=pk).exists():
                    queryset = Receita.objects.get(pk=pk)
                    serializer_class = ReceitaSerializer(queryset, data=request.data, partial=True)
                    if serializer_class.is_valid(raise_exception=True):
                        serializer_class.save()
                        return Response(serializer_class.data, status=status.HTTP_200_OK)
                else:
                    return Response(data="Este ID não existe", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data="O método PUT necessida de um ID como parâmetro", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk:
            if len(str(pk)) > 36 or len(str(pk)) < 36:
                return Response(data="ID inválido", status=status.HTTP_400_BAD_REQUEST)
            else:
                if Receita.objects.filter(pk=pk).exists():
                    queryset = Receita.objects.get(pk=pk)
                    queryset.delete()
                    return Response(data="Receita excluída", status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response(data="Este ID não existe", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data="O método DELETE necessita de um ID como parâmetro")

class DespesaAPIView(APIView):
    """API's de Despesas"""

    def get(self, request, pk=None):
        if pk:
            queryset = Despesa.objects.get(pk=pk)
            serializer_class = DespesaSerializer(queryset)
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        else:
            queryset = Despesa.objects.all()
            serializer_class = DespesaSerializer(queryset, many=True)
            return Response(serializer_class.data, status=status.HTTP_200_OK)

    def post(self, request):
        queryset = DespesaSerializer(data=request.data)
        queryset.is_valid(raise_exception=True)
        queryset.save()
        return Response(queryset.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None):
        if pk:
            if len(str(pk)) > 36 or len(str(pk)) < 36:
                return Response(data="ID inválido", status=status.HTTP_400_BAD_REQUEST)
            else:
                if Despesa.objects.filter(pk=pk).exists():
                    queryset = Despesa.objects.get(pk=pk)
                    serializer_class = DespesaSerializer(queryset, data=request.data, partial=True)
                    if serializer_class.is_valid(raise_exception=True):
                        serializer_class.save()
                        return Response(serializer_class.data, status=status.HTTP_200_OK)
                else:
                    return Response(data="Este ID não existe", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data="O método PUT necessida de um ID como parâmetro", status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk=None):
        if pk:
            if len(str(pk)) > 36 or len(str(pk)) < 36:
                return Response(data="ID inválido", status=status.HTTP_400_BAD_REQUEST)
            else:
                if Despesa.objects.filter(pk=pk).exists():
                    queryset = Despesa.objects.get(pk=pk)
                    queryset.delete()
                    return Response(data="Despesa excluída", status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response(data="Este ID não existe", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data="O método DELETE necessita de um ID como parâmetro")
