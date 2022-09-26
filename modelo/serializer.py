from dataclasses import field
from decimal import Decimal
from pyexpat import model
from select import select
from unicodedata import decimal
from unittest.util import _MAX_LENGTH
from rest_framework import serializers

from modelo.models import Cliente, Conta, Cartao, Movimentacoes, Emprestimo, PagamentoEmprestimos, Extrato

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf', 'data_nascimento', 'email', 'login', 'foto', 'data_cadastro', 'foto']


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['id', 'cliente', 'numeroConta', 'agencia', 'tipo', 'saldo']


class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao
        fields = ['id', 'conta', 'numeroCartao', 'validade', 'cvv', 'bandeira', 'bloqueado', 'tipoCartao']


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