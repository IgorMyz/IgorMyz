import random

numero_secreto = random.randint(1, 10)
tentativas = 3

print("Tente adivinhar o número entre 1 e 10.")

while tentativas > 0:
    palpite = int(input(f"Você tem {tentativas} tentativas. Qual é o número? "))
    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break
    else:
        print("Você errou!")
        tentativas -= 1

else:
    print(f"Você não conseguiu adivinhar o número. O número era {numero_secreto}. Na proxíma vez você consegue, NÃO DESISTA!")