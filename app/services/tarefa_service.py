from ..models import Tarefa

def cadastrar_tarefa(tarefa):
    Tarefa.objects.create(unidade=tarefa.unidade, fornecedor=tarefa.fornecedor, produto=tarefa.produto,
                          codigo_barra=tarefa.codigo_barra, data_fabricacao=tarefa.data_fabricacao, data_validade=tarefa.data_validade,
                          custo_unidade=tarefa.custo_unidade, quant_compra=tarefa.quant_compra, preco_venda=tarefa.preco_venda,
                          quant_venda=tarefa.quant_venda, perecibilidade= tarefa.perecibilidade, foto_produto=tarefa.foto_produto,
                          usuario=tarefa.usuario)

def index_tarefas():
    return Tarefa.objects.all()

def listar_tarefas(usuario):
    return Tarefa.objects.filter(usuario=usuario).all()

def listar_tarefa_id(id):
    return Tarefa.objects.get(id=id)

def editar_tarefa(tarefa_bd, tarefa_nova):
    tarefa_bd.unidade = tarefa_nova.unidade
    tarefa_bd.fornecedor = tarefa_nova.fornecedor
    tarefa_bd.produto = tarefa_nova.produto
    tarefa_bd.codigo_barra = tarefa_nova.codigo_barra
    tarefa_bd.data_fabricacao = tarefa_nova.data_fabricacao
    tarefa_bd.data_validade = tarefa_nova.data_validade
    tarefa_bd.custo_unidade = tarefa_nova.custo_unidade
    tarefa_bd.quant_compra = tarefa_nova.quant_compra
    tarefa_bd.preco_venda = tarefa_nova.preco_venda
    tarefa_bd.quant_venda = tarefa_nova.quant_venda
    tarefa_bd.perecibilidade = tarefa_nova.perecibilidade
    tarefa_bd.foto_produto = tarefa_nova.foto_produto
    tarefa_bd.save(force_update=True)

def remover_tarefa(tarefa_bd):
    tarefa_bd.delete()

def grafico_autor(usuario):
    return Tarefa.objects.filter(usuario=usuario).all().values()

