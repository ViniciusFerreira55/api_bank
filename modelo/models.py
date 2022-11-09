from distutils.command.upload import upload
import email
from msilib.schema import Class
from operator import mod
from pyexpat import model
from re import T
from tkinter import CASCADE
from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True)
    data_cadastro = models.DateField(auto_now=True)
    password = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='modelo/cliente')

class Conta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    numeroConta = models.CharField(max_length=50)
    agencia = models.CharField(max_length=50)
    CORRENTE = 'C'
    POUPANCA = 'P'

    TIPOS_CONTA = [
        (CORRENTE, 'Corrente'),
        (POUPANCA, 'Poupança')
    ]
    tipo = models.CharField(max_length=1, choices=TIPOS_CONTA, default=CORRENTE)
    saldo = models.DecimalField(max_digits=9, decimal_places=2)

class Cartao(models.Model):
    DEBITO = 'D'
    CREDITO = 'C'

    TIPO_CARTAO = [
        (DEBITO, 'Debito'),
        (CREDITO, 'Credito')
    ]

    conta = models.ForeignKey(Conta, on_delete=models.PROTECT)
    numeroCartao = models.CharField(max_length=25)
    validade = models.DateField()
    cvv = models.CharField(max_length=4)
    bandeira = models.CharField(max_length=25)
    bloqueado = models.BooleanField(default=False)
    tipoCartao = models.CharField(max_length=1, choices=TIPO_CARTAO, default=DEBITO)

class Movimentacoes(models.Model):
    data_movimentacao = models.DateField()
    operacoes = models.CharField(max_length=45)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    contaDebitada = models.ForeignKey(Conta, on_delete=models.PROTECT, related_name='contaDebitada')
    contaCreditada = models.ForeignKey(Conta, on_delete=models.PROTECT, related_name='contaCreditada')

class Emprestimo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    valorSolicitado = models.DecimalField(max_digits=9, decimal_places=2)
    data_solicitacao = models.DateField()
    taxa = models.DecimalField(max_digits=9, decimal_places=2)
    aprovado = models.BooleanField(default=False)
    qtdParcela = models.IntegerField()
    valorJuros = models.DecimalField(max_digits=9, decimal_places=2)
    data_primeira = models.DateField()
    situacao = models.CharField(max_length=45)
    qtdParcelasPagas = models.IntegerField()
    valorTotalPago = models.DecimalField(max_digits=9, decimal_places=2)
class PagamentoEmprestimos(models.Model):
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    data_pagamento = models.DateField()

class Extrato(models.Model):
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.PROTECT)
    movimentacao = models.ForeignKey(Movimentacoes, on_delete=models.PROTECT)


# class Imagens(models.Model):
#     titulo = models.CharField(max_length=255)
    
#     def __str__(self):
#         return self.titulo

