from calculadora import*
def mostrar_menu():
    print("Escolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def obter_opcao():
    while True:
        try:
            opcao = int(input("Digite o número da operação desejada: "))
            if opcao in [1, 2, 3, 4, 5]:
                return opcao
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def obter_valores():
    while True:
        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            return a, b
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def main():
    while True:
        mostrar_menu()
        opcao = obter_opcao()
        
        if opcao == 5:
            print("Saindo...")
            break
        
        a, b = obter_valores()
        
        if opcao == 1:
            resultado = somar(a, b)
            print(f"Resultado da soma: {resultado}")
        elif opcao == 2:
            resultado = subtrair(a, b)
            print(f"Resultado da subtração: {resultado}")
        elif opcao == 3:
            resultado = multiplicar(a, b)
            print(f"Resultado da multiplicação: {resultado}")
        elif opcao == 4:
            try:
                resultado = dividir(a, b)
                print(f"Resultado da divisão: {resultado}")
            except ValueError as e:
                print(e)

if __name__ == "__main__":
    main()

 