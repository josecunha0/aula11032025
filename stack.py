from typing import Optional, List, Dict
from models import Nodo, Compra

class PilhaDinamica:
    def __init__(self):
        self.topo = None
        self.tamanho = 0
    
    def esta_vazia(self) -> bool:
        return self.topo is None
    
    def empilhar(self, compra: Compra) -> None:
        """Adiciona uma nova compra no topo da pilha"""
        novo_nodo = Nodo(compra)
        novo_nodo.proximo = self.topo
        self.topo = novo_nodo
        self.tamanho += 1
    
    def desempilhar(self) -> Optional[Compra]:
        """Remove e retorna a compra do topo da pilha"""
        if self.esta_vazia():
            return None
        
        compra = self.topo.compra
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return compra
    
    def obter_topo(self) -> Optional[Compra]:
        """Retorna a compra do topo sem removê-la"""
        if self.esta_vazia():
            return None
        return self.topo.compra
    
    def processar_venda(self, produto: str, quantidade: int) -> tuple[float, List[str]]:
        """
        Processa uma venda, atualizando o estoque e retornando o valor total da venda
        e um log das operações realizadas. O valor de venda é sempre baseado na última compra.
        """
        if self.esta_vazia():
            raise ValueError(f"Não há estoque disponível para o produto {produto}")
        
        # Obtém o valor de venda do último lote (topo da pilha)
        compra_topo = self.obter_topo()
        if compra_topo.produto != produto:
            raise ValueError(f"O produto no topo da pilha ({compra_topo.produto}) é diferente do produto vendido ({produto})")
        
        valor_venda_unitario = compra_topo.valor_venda
        valor_total = 0
        quantidade_restante = quantidade
        log_operacoes = []
        
        while quantidade_restante > 0 and not self.esta_vazia():
            compra_atual = self.obter_topo()
            
            if compra_atual.produto != produto:
                raise ValueError(f"O produto no topo da pilha ({compra_atual.produto}) é diferente do produto vendido ({produto})")
            
            if compra_atual.quantidade >= quantidade_restante:
                # Temos estoque suficiente no topo
                valor_desta_venda = quantidade_restante * valor_venda_unitario
                compra_atual.quantidade -= quantidade_restante
                valor_total += valor_desta_venda
                log_operacoes.append(f"Vendido {quantidade_restante} unidades do lote com valor unitário R${valor_venda_unitario:.2f}")
                quantidade_restante = 0
                
                if compra_atual.quantidade == 0:
                    self.desempilhar()
            else:
                # Precisamos usar todo o estoque do topo e continuar com o próximo
                valor_desta_venda = compra_atual.quantidade * valor_venda_unitario
                valor_total += valor_desta_venda
                log_operacoes.append(f"Vendido {compra_atual.quantidade} unidades do lote com valor unitário R${valor_venda_unitario:.2f}")
                quantidade_restante -= compra_atual.quantidade
                self.desempilhar()
        
        if quantidade_restante > 0:
            raise ValueError(f"Estoque insuficiente. Faltam {quantidade_restante} unidades para completar a venda")
        
        return valor_total, log_operacoes
    
    def listar_estoque(self) -> List[str]:
        """Retorna uma lista com o estoque consolidado por produto"""
        produtos: Dict[str, dict] = {}
        atual = self.topo
        
        while atual:
            produto = atual.compra.produto
            if produto not in produtos:
                # Para cada produto novo, usamos os valores da última compra (primeiro encontrado na pilha)
                valor_unitario = atual.compra.valor_compra / atual.compra.quantidade
                produtos[produto] = {
                    'quantidade': 0,
                    'valor_unitario_ultima_compra': valor_unitario,
                    'data_ultima_compra': atual.compra.data
                }
            
            produtos[produto]['quantidade'] += atual.compra.quantidade
            atual = atual.proximo
        
        resultado = []
        for produto, info in produtos.items():
            if info['quantidade'] > 0:  # Só mostra produtos com estoque
                valor_venda_unitario = info['valor_unitario_ultima_compra'] * 1.3  # 30% de margem
                resultado.append(
                    f"Data última compra: {info['data_ultima_compra'].strftime('%d/%m/%Y')}, "
                    f"Produto: {produto}, "
                    f"Quantidade total: {info['quantidade']}, "
                    f"Valor última compra: R${info['valor_unitario_ultima_compra']:.2f}, "
                    f"Valor venda: R${valor_venda_unitario:.2f}"
                )
        
        return resultado 