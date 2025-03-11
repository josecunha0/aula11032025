# Sistema de Gerenciamento de Estoque com Pilha Dinâmica

## Introdução
Desenvolvi este sistema para gerenciar o estoque de um supermercado usando o conceito de pilha dinâmica. A ideia principal é manter um controle preciso das compras e vendas, onde os produtos mais recentemente comprados são os primeiros a serem vendidos (LIFO - Last In, First Out).

## Como o Sistema Funciona

### Estrutura de Dados
O sistema utiliza uma pilha dinâmica implementada através de uma lista encadeada. Cada nó da pilha contém:
- Informações da compra (data, produto, valores, quantidade)
- Ponteiro para o próximo nó

Escolhi essa estrutura porque ela é perfeita para nosso caso de uso: quando fazemos uma venda, sempre queremos usar primeiro o estoque mais recente. A pilha naturalmente nos dá isso, já que o topo sempre contém a última compra realizada.

### Principais Funcionalidades

#### 1. Registro de Compras
Quando registramos uma compra, criamos um novo nó e o colocamos no topo da pilha. Por exemplo:

```python
Data: 25/03/2024
Produto: Arroz
Valor de compra: R$ 100,00
Quantidade: 10 unidades
```

O sistema automaticamente:
- Calcula o valor unitário (R$ 10,00 por unidade)
- Define o valor de venda (R$ 13,00 por unidade, margem de 30%)
- Coloca essa compra no topo da pilha
- Atualiza o valor de venda para todos os lotes existentes deste produto

#### 2. Registro de Vendas
O processo de venda é mais interessante. Vamos supor que temos:
- Lote 1: 20 unidades de arroz
- Lote 2: 10 unidades de arroz (mais recente, R$ 10,00 cada)

Se vendermos 25 unidades, o sistema:
1. Usa primeiro as 10 unidades do lote mais recente
2. Depois usa 15 unidades do lote anterior
3. Calcula o valor total baseado no preço de venda atual (R$ 13,00 por unidade para todas as unidades)

Importante: O valor de venda é SEMPRE baseado na última compra, independentemente do lote que está sendo vendido.

#### 3. Consulta de Estoque
A consulta mostra um resumo consolidado por produto. Por exemplo:
```
Data última compra: 25/03/2024
Produto: Arroz
Quantidade total: 30 unidades
Valor última compra: R$ 10,00
Valor venda: R$ 13,00
```

## Como Rodar o Sistema

### Requisitos
- Python 3.6 ou superior
- Não precisa instalar nenhuma biblioteca adicional

### Passo a Passo
1. Baixe os arquivos do projeto
2. Abra o terminal na pasta do projeto
3. Execute o comando:
   ```bash
   python main.py
   ```

### Usando o Sistema
Ao iniciar, você verá um menu com 4 opções:
1. Registrar Compra
2. Registrar Venda
3. Exibir Estoque
4. Sair

Para testar, sugiro:
1. Registre algumas compras do mesmo produto com valores diferentes
2. Faça uma consulta do estoque para ver como ficou
3. Registre uma venda e veja como o sistema gerencia os diferentes lotes

## Detalhes Técnicos Importantes

### Cálculo de Valores
- O valor de venda é SEMPRE baseado na última compra, para todos os lotes
- A margem é fixa em 30%
- Quando uma nova compra é registrada, seu valor de venda se torna o valor padrão para todas as vendas daquele produto

### Validações
O sistema impede:
- Vendas maiores que o estoque disponível
- Valores negativos ou zero
- Vendas de produtos inexistentes

## Dicas de Uso
- Mantenha um registro das compras em ordem cronológica
- Verifique o estoque antes de fazer vendas grandes
- Lembre-se que ao fazer uma nova compra, o valor de venda de TODO o estoque daquele produto será atualizado
- O sistema sempre usa o estoque mais recente primeiro (LIFO)

## Sugestões de Melhorias Futuras
- Adicionar relatórios de vendas
- Implementar busca por data
- Criar backup automático dos dados
- Adicionar categorias de produtos 
