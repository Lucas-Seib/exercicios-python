import random

num = random.randint(0,5)

chute = int(input("Chute o número que a máquina escolheu: "))

if chute == num:
    print("Você ACERTOU!")
else:
    print(f"Você ERROU! Eu pensei no número {num} e não no {chute}")
