from datetime import datetime

class Compra:
    def __init__(self, data: datetime, produto: str, valor_compra: float, quantidade: int):
        self.data = data
        self.produto = produto
        self.valor_compra = valor_compra
        self.quantidade = quantidade
        self.valor_venda = self.calcular_valor_venda()
    
    def calcular_valor_venda(self) -> float:
        """Calcula o valor de venda unitário com margem de 30%"""
        valor_unitario = self.valor_compra / self.quantidade
        return valor_unitario * 1.3
    
    def __str__(self) -> str:
        valor_unitario = self.valor_compra / self.quantidade
        return f"Data: {self.data.strftime('%d/%m/%Y')}, Produto: {self.produto}, " \
               f"Quantidade: {self.quantidade}, Valor Compra Unit.: R${valor_unitario:.2f}, " \
               f"Valor Venda Unit.: R${self.valor_venda:.2f}"

class Nodo:
    def __init__(self, compra: Compra):
        self.compra = compra
        self.proximo = None 