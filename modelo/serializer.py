from dataclasses import field
from decimal import Decimal
from pyexpat import model
from select import select
from unicodedata import decimal
from unittest.util import _MAX_LENGTH
from rest_framework import serializers

from modelo.models import Cliente, Conta, Movimentacoes, Emprestimo, PagamentoEmprestimos, Extrato

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf', 'data_nascimento', 'email', 'password', 'data_cadastro']

class Loginserializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'cpf', 'password']

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['id', 'cliente', 'numeroConta', 'agencia', 'tipo', 'saldo', "numeroCartao", "validade", 'cvv']

class CreateContaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    class Meta:
        model = Conta
        fields = '__all__'
    
    def create(self, validated_data):
        cliente_dict = validated_data.pop('cliente')

        cliente = Cliente.objects.create(**cliente_dict)
        conta_instance = Conta.objects.create(
            cliente=cliente, **validated_data
        )
        return conta_instance



class MovimentacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimentacoes
        fields = ['id', 'data_movimentacao', 'operacoes', 'valor', 'contaDebitada', 'contaCreditada']


class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = ['id', 'cliente', 'valorSolicitado', 'data_solicitacao', 'taxa', 'aprovado', 'qtdParcela', 'valorJuros', 'data_primeira', 'situacao', 'qtdParcelasPagas', 'valorTotalPago']


class PagamentoEmprestimosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagamentoEmprestimos
        fields = ['id', 'emprestimo', 'valor', 'data_pagamento']


class ExtratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extrato
        fields = ['id', 'emprestimo', 'movimentacao']

    
# class ImagensSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Imagens
#         fields = ['id', 'titulo', 'foto']