from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cliente, Conta, Cartao, Imagens, Movimentacoes, Emprestimo, PagamentoEmprestimos, Extrato
from .serializer import ClienteSerializer, ContaSerializer, CartaoSerializer, ImagensSerializer, MovimentacoesSerializer, EmprestimoSerializer, PagamentoEmprestimosSerializer, ExtratoSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
# Create your views here.


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

class CartaoViewSet(viewsets.ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer

class MovimentacoesViewSet(viewsets.ModelViewSet):
    queryset = Movimentacoes.objects.all()
    serializer_class = MovimentacoesSerializer

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class PagamentoEmprestimosViewSet(viewsets.ModelViewSet):
    queryset = PagamentoEmprestimos.objects.all()
    serializer_class = PagamentoEmprestimosSerializer

class ExtratoViewSet(viewsets.ModelViewSet):
    queryset = Extrato.objects.all()
    serializer_class = ExtratoSerializer

class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagens.objects.all()
    serializer_class = ImagensSerializer