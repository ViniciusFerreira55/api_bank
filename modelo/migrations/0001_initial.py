# Generated by Django 4.1.1 on 2022-09-21 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11)),
                ('data_nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('login', models.CharField(max_length=255)),
                ('foto', models.ImageField(upload_to='')),
                ('data_cadastro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroConta', models.CharField(max_length=50)),
                ('agencia', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('C', 'Corrente'), ('P', 'Poupança')], default='C', max_length=1)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=9)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modelo.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valorSolicitado', models.DecimalField(decimal_places=2, max_digits=9)),
                ('data_solicitacao', models.DateField()),
                ('taxa', models.DecimalField(decimal_places=2, max_digits=9)),
                ('aprovado', models.BooleanField(default=False)),
                ('qtdParcela', models.IntegerField()),
                ('valorJuros', models.DecimalField(decimal_places=2, max_digits=9)),
                ('data_primeira', models.DateField()),
                ('situacao', models.CharField(max_length=45)),
                ('qtdParcelasPagas', models.IntegerField()),
                ('valorTotalPago', models.DecimalField(decimal_places=2, max_digits=9)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modelo.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='PagamentoEmprestimos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9)),
                ('data_pagamento', models.DateField()),
                ('emprestimo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modelo.emprestimo')),
            ],
        ),
        migrations.CreateModel(
            name='Movimentacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_movimentacao', models.DateField()),
                ('operacoes', models.CharField(max_length=45)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9)),
                ('contaCreditada', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contaCreditada', to='modelo.conta')),
                ('contaDebitada', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contaDebitada', to='modelo.conta')),
            ],
        ),
        migrations.CreateModel(
            name='Extrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emprestimo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modelo.emprestimo')),
                ('movimentacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modelo.movimentacoes')),
            ],
        ),
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroCartao', models.CharField(max_length=25)),
                ('validade', models.DateField()),
                ('cvv', models.CharField(max_length=4)),
                ('bandeira', models.CharField(max_length=25)),
                ('bloqueado', models.BooleanField(default=False)),
                ('tipoCartão', models.CharField(choices=[('D', 'Debito'), ('C', 'Credito')], default='D', max_length=1)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modelo.conta')),
            ],
        ),
    ]
