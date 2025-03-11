from datetime import datetime
from models import Compra
from stack import PilhaDinamica

def exibir_menu():
    print("\n=== Sistema de Gerenciamento de Compras e Estoque ===")
    print("1. Registrar Compra")
    print("2. Registrar Venda")
    print("3. Exibir Estoque")
    print("4. Sair")
    return input("Escolha uma opção: ")

def registrar_compra(pilha: PilhaDinamica):
    print("\n=== Registro de Compra ===")
    try:
        data = datetime.strptime(input("Data (DD/MM/AAAA): "), "%d/%m/%Y")
        produto = input("Produto: ")
        valor_compra = float(input("Valor de compra: R$"))
        quantidade = int(input("Quantidade: "))
        
        if valor_compra <= 0 or quantidade <= 0:
            print("Erro: Valor de compra e quantidade devem ser maiores que zero!")
            return
        
        compra = Compra(data, produto, valor_compra, quantidade)
        pilha.empilhar(compra)
        print("\nCompra registrada com sucesso!")
        print(f"Valor de venda calculado: R${compra.valor_venda:.2f}")
        
    except ValueError as e:
        print(f"\nErro ao registrar compra: {str(e)}")

def registrar_venda(pilha: PilhaDinamica):
    print("\n=== Registro de Venda ===")
    try:
        produto = input("Produto: ")
        quantidade = int(input("Quantidade: "))
        
        if quantidade <= 0:
            print("Erro: Quantidade deve ser maior que zero!")
            return
        
        valor_total, log_operacoes = pilha.processar_venda(produto, quantidade)
        
        print("\nVenda processada com sucesso!")
        print(f"Valor total da venda: R${valor_total:.2f}")
        print("\nDetalhes da operação:")
        for log in log_operacoes:
            print(f"- {log}")
            
    except ValueError as e:
        print(f"\nErro ao processar venda: {str(e)}")

def main():
    pilha = PilhaDinamica()
    
    while True:
        opcao = exibir_menu()
        
        if opcao == "1":
            registrar_compra(pilha)
        elif opcao == "2":
            registrar_venda(pilha)
        elif opcao == "3":
            print("\n=== Estoque Atual ===")
            estoque = pilha.listar_estoque()
            if not estoque:
                print("Estoque vazio!")
            else:
                for item in estoque:
                    print(item)
        elif opcao == "4":
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOpção inválida!")

if __name__ == "__main__":
    main() 