from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..forms import TarefaForm
from ..entidades.tarefa import Tarefa
from ..services import tarefa_service
# Create your views here.

def index_tarefas(request):
    i_tarefas= tarefa_service.index_tarefas()
    return render(request, 'tarefas/index_tarefas.html', {"i_tarefas":i_tarefas})

@login_required()
def listar_tarefas(request):
    if request.method == 'GET':
        tarefas = tarefa_service.listar_tarefas(request.user)
    return render(request, 'tarefas/listar_tarefas.html', {"tarefas":tarefas})

@login_required()
def cadastrar_tarefa(request):
    if request.method == "POST":
        form_tarefa = TarefaForm(request.POST, request.FILES)
        if form_tarefa.is_valid():
            unidade = form_tarefa.cleaned_data["unidade"]
            fornecedor = form_tarefa.cleaned_data["fornecedor"]
            produto = form_tarefa.cleaned_data["produto"]
            codigo_barra = form_tarefa.cleaned_data["codigo_barra"]
            data_fabricacao = form_tarefa.cleaned_data["data_fabricacao"]
            data_validade = form_tarefa.cleaned_data["data_validade"]
            custo_unidade = form_tarefa.cleaned_data["custo_unidade"]
            quant_compra = form_tarefa.cleaned_data["quant_compra"]
            preco_venda = form_tarefa.cleaned_data["preco_venda"]
            quant_venda = form_tarefa.cleaned_data["quant_venda"]
            perecibilidade = form_tarefa.cleaned_data["perecibilidade"]
            foto_produto  = form_tarefa.cleaned_data["foto_produto"]
            tarefa_nova = Tarefa(unidade=unidade, fornecedor=fornecedor, produto=produto,
                                 codigo_barra=codigo_barra, data_fabricacao=data_fabricacao, data_validade= data_validade,
                                 custo_unidade=custo_unidade, quant_compra=quant_compra,  preco_venda=preco_venda,
                                 quant_venda=quant_venda, perecibilidade=perecibilidade, foto_produto=foto_produto,
                                 usuario=request.user)
            tarefa_service.cadastrar_tarefa(tarefa_nova)
            return redirect('listar_tarefas')
    else:
        form_tarefa = TarefaForm()
    return render(request, 'tarefas/form_tarefa.html', {"form_tarefa": form_tarefa})

@login_required()
def editar_tarefa(request, id):
    tarefa_bd = tarefa_service.listar_tarefa_id(id)
    if tarefa_bd.usuario != request.user:
        return HttpResponse("Não permitido")
    form_tarefa = TarefaForm(request.POST or None, instance=tarefa_bd)
    if form_tarefa.is_valid():
        unidade = form_tarefa.cleaned_data["unidade"]
        fornecedor = form_tarefa.cleaned_data["fornecedor"]
        produto = form_tarefa.cleaned_data["produto"]
        codigo_barra = form_tarefa.cleaned_data["codigo_barra"]
        data_fabricacao = form_tarefa.cleaned_data["data_fabricacao"]
        data_validade = form_tarefa.cleaned_data["data_validade"]
        custo_unidade = form_tarefa.cleaned_data["custo_unidade"]
        quant_compra = form_tarefa.cleaned_data["quant_compra"]
        preco_venda = form_tarefa.cleaned_data["preco_venda"]
        quant_venda = form_tarefa.cleaned_data["quant_venda"]
        perecibilidade = form_tarefa.cleaned_data["perecibilidade"]
        foto_produto = form_tarefa.cleaned_data["foto_produto"]
        tarefa_nova = Tarefa(unidade=unidade, fornecedor=fornecedor, produto=produto,
                             codigo_barra=codigo_barra, data_fabricacao=data_fabricacao, data_validade=data_validade,
                             custo_unidade=custo_unidade, quant_compra=quant_compra, preco_venda=preco_venda,
                             quant_venda=quant_venda, perecibilidade=perecibilidade, foto_produto=foto_produto,
                             usuario=request.user)
        tarefa_service.editar_tarefa(tarefa_bd, tarefa_nova)
        return redirect('listar_tarefas')
    return render(request, 'tarefas/form_tarefa.html', {"form_tarefa": form_tarefa})

@login_required()
def remover_tarefa(request, id):
    tarefa_bd = tarefa_service.listar_tarefa_id(id)
    if request.method == "POST":
        tarefa_service.remover_tarefa(tarefa_bd)
        return redirect('listar_tarefas')
    return render(request,'tarefas/confirma_exclusao.html', {'tarefa': tarefa_bd})









