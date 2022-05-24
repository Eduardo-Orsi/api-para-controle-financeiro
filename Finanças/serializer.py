from asyncio.windows_events import NULL
from rest_framework import serializers
from Finanças.models import Receita, Despesa, CategoriaDespesa, CategoriaReceita

class ReceitaSerializer(serializers.ModelSerializer):
    
    data = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y', 'iso-8601'])

    def validate(self, data_entry):
        queryset = Receita.objects.filter(data__month=data_entry['data'].month)
        for data in queryset:
            if data_entry['descricao'] == data.descricao:
                if data_entry['data'].month == data.data.month:
                    raise serializers.ValidationError("Você não pode ter duas despesas iguais no mesmo mês.")
        return data_entry

    class Meta:
        model = Receita
        fields = '__all__'

class CategoriaReceitaSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoriaReceita
        fields = '__all__'


class DespesaSerializer(serializers.ModelSerializer):

    data = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y', 'iso-8601'])

    def validate(self, data_entry):
        queryset = Despesa.objects.filter(data__month=data_entry['data'].month)
        for data in queryset:
            if data_entry['descricao'] == data.descricao:
                if data_entry['data'].month == data.data.month:
                    raise serializers.ValidationError("Você não pode ter duas despesas iguais no mesmo mês.")

        if data_entry['categoria']:
            return data_entry
        else:
            data_entry['categoria'] = CategoriaDespesa.objects.get(nome='Outras')
            return data_entry

    class Meta:
        model = Despesa
        fields = '__all__'

class CategoriaDespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaDespesa
        fields = '__all__'