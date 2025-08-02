import random

n = random.randint(1,10)
r = ""
tentativas = 0

while r != n:
    r = int(input("Digite o número: "))
    tentativas = tentativas + 1
    print("Você errou! Tente novamente.")
print(f"Você acertou! O número que eu escolhi foi {n}.")
print(f"Você precisou de {tentativas} tentativas para acertar!")