from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cliente, Conta, Cartao, Movimentacoes, Emprestimo, PagamentoEmprestimos, Extrato
from .serializer import ClienteSerializer, ContaSerializer, CartaoSerializer, MovimentacoesSerializer, EmprestimoSerializer, PagamentoEmprestimosSerializer, ExtratoSerializer, Loginserializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
# Create your views here.


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def create(self, request, *args, **kwargs):
        print(self.request.data)
        return super().create(request, *args, **kwargs)

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

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = Loginserializer

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        listaClientes = Cliente.objects.all()
        for c in listaClientes:
            if self.request.data['cpf'] == c.cpf and self.request.data['password'] == c.password:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
                
        # return super().create(request, *args, **kwargs)
# class ImagemViewSet(viewsets.ModelViewSet):
#     queryset = Imagens.objects.all()
#     serializer_class = ImagensSerializer