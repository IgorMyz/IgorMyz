inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))


soma_pares = 0


for num in range(inicio, fim + 1):
    if num % 2 == 0:
        soma_pares += num


if soma_pares == 0:
    print("Não há números pares no intervalo.")
else:
    print("A soma dos números pares no intervalo é:", soma_pares)
