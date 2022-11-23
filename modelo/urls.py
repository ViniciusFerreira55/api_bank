from ast import Import
from django import views 
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('clientes', views.ClienteViewSet, basename='cliente')
router.register('conta', views.ContaViewSet, basename='conta')
router.register('movimentacao', views.MovimentacoesViewSet, basename='movimentacao')
router.register('emprestimo', views.EmprestimoViewSet, basename='emprestimo')
router.register('pagamento', views.PagamentoEmprestimosViewSet, basename='pagamento')
router.register('extrato', views.ExtratoViewSet, basename='extrato')
router.register('login', views.LoginViewSet, basename='login')
# router.register('imagens', views.ImagemViewSet, basename='imagens')
urlpatterns = router.urls