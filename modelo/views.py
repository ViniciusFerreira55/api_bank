from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cliente, Conta, Cartao, Movimentacoes, Emprestimo, PagamentoEmprestimos, Extrato
from .serializer import ClienteSerializer, ContaSerializer, CreateContaSerializer, CartaoSerializer, MovimentacoesSerializer, EmprestimoSerializer, PagamentoEmprestimosSerializer, ExtratoSerializer, Loginserializer
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

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateContaSerializer
        return ContaSerializer

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
        encontrou = False
        for c in listaClientes:

            if self.request.data['cpf'] == c.cpf and self.request.data['password'] == c.password:
                
                _conta = Conta.objects.get(cliente=c)
                cli = _conta.cliente

                conta = {
                    'numeroConta': _conta.numeroConta,
                    'agencia': _conta.agencia,
                    'tipo': _conta.tipo,
                    'saldo': _conta.saldo,
                    'cliente': {
                    'nome': cli.nome,
                    'cpf': cli.cpf,
                    'data_nascimento': cli.data_nascimento,
                    'email': cli.email,
                    'data_cadastro': cli.data_cadastro,
                    'password': cli.password
                    }
                }
                encontrou = True
                return Response({ 'conta': conta },status=status.HTTP_200_OK)
            # else:
              
        if not encontrou:
              return Response({ 'conta': None } ,status=status.HTTP_200_OK)                
        # return super().create(request, *args, **kwargs)
# class ImagemViewSet(viewsets.ModelViewSet):
#     queryset = Imagens.objects.all()
#     serializer_class = ImagensSerializer