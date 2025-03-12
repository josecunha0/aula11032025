# Exemplos Práticos de Uso do Sistema

## Caso 1: Gerenciando Estoque de Arroz

### Primeira Compra
```
Opção: 1
Data: 20/03/2024
Produto: Arroz
Valor de compra: R$ 150,00
Quantidade: 30 unidades

>> Sistema calcula:
   Valor unitário: R$ 5,00
   Valor de venda: R$ 6,50
```

### Segunda Compra (Preço Diferente)
```
Opção: 1
Data: 25/03/2024
Produto: Arroz
Valor de compra: R$ 200,00
Quantidade: 20 unidades

>> Sistema calcula:
   Valor unitário: R$ 10,00
   Valor de venda: R$ 13,00
   
>> Todo o estoque de Arroz (50 unidades) agora tem valor de venda de R$ 13,00
```

### Consultando Estoque
```
Opção: 3

>> Sistema mostra:
Data última compra: 25/03/2024
Produto: Arroz
Quantidade total: 50 unidades
Valor última compra: R$ 10,00
Valor venda: R$ 13,00
```

### Realizando uma Venda
```
Opção: 2
Produto: Arroz
Quantidade: 25 unidades

>> Sistema processa:
- Vende 20 unidades do lote mais recente (R$ 13,00 cada)
- Vende 5 unidades do lote anterior (também R$ 13,00 cada)
- Mostra valor total: R$ 325,00 (25 unidades × R$ 13,00)
```

## Caso 2: Tratando Erros Comuns

### Tentativa de Venda Maior que Estoque
```
Opção: 2
Produto: Arroz
Quantidade: 100 unidades

>> Sistema mostra:
Erro: Estoque insuficiente. Faltam 60 unidades para completar a venda
```

### Valor de Compra Inválido
```
Opção: 1
Data: 25/03/2024
Produto: Feijão
Valor de compra: -50,00

>> Sistema mostra:
Erro: Valor de compra deve ser maior que zero!
```

## Caso 3: Múltiplos Produtos

### Comprando Produtos Diferentes
```
1. Arroz:
   Data: 25/03/2024
   Quantidade: 30
   Valor: R$ 150,00 (R$ 5,00 por unidade)
   Valor de venda: R$ 6,50 por unidade

2. Feijão:
   Data: 25/03/2024
   Quantidade: 20
   Valor: R$ 200,00 (R$ 10,00 por unidade)
   Valor de venda: R$ 13,00 por unidade
```

### Nova Compra de Arroz (Preço Maior)
```
Data: 26/03/2024
Quantidade: 10
Valor: R$ 80,00 (R$ 8,00 por unidade)
Valor de venda: R$ 10,40 por unidade

>> Todo o estoque de Arroz (40 unidades) agora tem valor de venda de R$ 10,40
```

### Consultando Estoque Múltiplo
```
Opção: 3

>> Sistema mostra:
1. Data última compra: 26/03/2024
   Produto: Arroz
   Quantidade total: 40 unidades
   Valor última compra: R$ 8,00
   Valor venda: R$ 10,40

2. Data última compra: 25/03/2024
   Produto: Feijão
   Quantidade total: 20 unidades
   Valor última compra: R$ 10,00
   Valor venda: R$ 13,00
```
