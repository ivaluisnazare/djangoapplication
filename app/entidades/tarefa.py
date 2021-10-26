class Tarefa():
    def __init__(self, unidade, fornecedor, produto, codigo_barra, data_fabricacao, data_validade,
                 custo_unidade, quant_compra, preco_venda, quant_venda, perecibilidade, foto_produto, usuario):

        self.__unidade = unidade
        self.__fornecedor = fornecedor
        self.__produto = produto
        self.__codigo_barra = codigo_barra
        self.__data_fabricacao = data_fabricacao
        self.__data_validade = data_validade
        self.__custo_unidade = custo_unidade
        self.__quant_compra = quant_compra
        self.__preco_venda = preco_venda
        self.__quant_venda = quant_venda
        self.__perecibilidade = perecibilidade
        self.__foto_produto = foto_produto
        self.__usuario = usuario

    @property
    def unidade(self):
        return self.__unidade
    @unidade.setter
    def unidade(self, unidade):
        self.__unidade=unidade

    @property
    def fornecedor(self):
        return self.__fornecedor
    @fornecedor.setter
    def fornecedor(self, fornecedor):
        self.__fornecedor=fornecedor

    @property
    def produto(self):
        return self.__produto
    @produto.setter
    def produto(self, produto):
        self.__produto=produto

    @property
    def codigo_barra(self):
        return self.__codigo_barra
    @codigo_barra.setter
    def codigo_barra(self, codigo_barra):
        self.__codigo_barra=codigo_barra

    @property
    def data_fabricacao(self):
        return self.__data_fabricacao
    @data_fabricacao.setter
    def data_fabricacao(self, data_fabricacao):
        self.__data_fabricacao=data_fabricacao

    @property
    def data_validade(self):
        return self.__data_validade
    @data_validade.setter
    def data_validade(self, data_validade):
        self.__data_validade=data_validade

    @property
    def custo_unidade(self):
        return self.__custo_unidade
    @custo_unidade.setter
    def custo_unidade(self, custo_unidade):
        self.__custo_unidade=custo_unidade

    @property
    def quant_compra(self):
        return self.__quant_compra
    @quant_compra.setter
    def quant_compra(self, quant_compra):
        self.__quant_compra=quant_compra

    @property
    def preco_venda(self):
        return self.__preco_venda
    @preco_venda.setter
    def preco_venda(self, preco_venda):
        self.__preco_venda=preco_venda

    @property
    def quant_venda(self):
        return self.__quant_venda
    @quant_venda.setter
    def quant_venda(self, quant_venda):
        self.__quant_venda = quant_venda

    @property
    def perecibilidade(self):
        return self.__perecibilidade
    @perecibilidade.setter
    def perecibilidade(self, perecibilidade):
        self.__perecibilidade = perecibilidade

    @property
    def foto_produto(self):
        return self.__foto_produto
    @foto_produto.setter
    def foto_produto(self, foto_produto):
        self.__foto_produto = foto_produto


    @property
    def usuario(self):
        return self.__usuario
    @usuario.setter
    def usuario(self, usuario):
        self.__usuario=usuario
