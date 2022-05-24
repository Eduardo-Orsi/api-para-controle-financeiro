from django.contrib import admin
from Finanças.models import Receita, Despesa, CategoriaDespesa, CategoriaReceita

class Receitas(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'data')
    list_display_links = ('descricao',)
    search_fields = ('descricao', 'valor', 'data',)
    list_per_page = 25

admin.site.register(Receita, Receitas)

class Despesas(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'data')
    list_display_links = ('descricao',)
    search_fields = ('descricao', 'valor', 'data',)
    list_per_page = 25

admin.site.register(Despesa, Despesas)

class CategoriasReceitas(admin.ModelAdmin):
    list_display = ('nome', 'id')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 25

admin.site.register(CategoriaReceita, CategoriasReceitas)

class CategoriasDespesas(admin.ModelAdmin):
    list_display = ('nome', 'id')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 25

admin.site.register(CategoriaDespesa, CategoriasDespesas)
