# Generated by Django 4.0.3 on 2022-04-26 14:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Finanças', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaDespesa',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaReceita',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='despesa',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Finanças.categoriadespesa'),
        ),
        migrations.AddField(
            model_name='receita',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Finanças.categoriareceita'),
        ),
    ]
