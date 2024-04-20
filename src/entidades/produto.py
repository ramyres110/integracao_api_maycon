import json

'''
Entidade classe Produto
'''
class Produto:
    
    def __init__(self, codigo_interno, SKU, descricao, fornecedor, saldo, preco_operacional):
        self.codigo_interno = codigo_interno
        self.SKU = SKU
        self.descricao = descricao
        self.fornecedor = fornecedor
        self.saldo = self.format_saldo(saldo)
        self.preco_operacional = self.format_preco_operacional(preco_operacional)

    def __str__(self) -> str:
        return f'''
            codigo_interno:{self.codigo_interno},
            SKU:{self.SKU},
            descricao:{self.descricao},
            fornecedor:{self.fornecedor},
            saldo:{self.saldo},
            preco_operacional:{self.preco_operacional},
        '''

    def format_preco_operacional(self, preco):
        if type(preco) == str:
            return float(preco.replace(',', '.'))
        elif type(preco) == float:
            return preco
        else:
            raise ValueError("Preco operacional inválido!")
        
    def format_saldo(self, saldo):
        if type(saldo) == str:
            return int(saldo)
        elif type(saldo) == int:
            return saldo
        else:
            raise ValueError("Valor do saldo inválido!")
        
    def asTuple(self) -> tuple:
        return  (
            self.codigo_interno,
            self.SKU,
            self.descricao,
            self.fornecedor,
            self.saldo,
            self.preco_operacional
        )
    
    def asJson(self):
        return json.dumps(
            self,
            default = lambda obj: obj.__dict__,
        )

