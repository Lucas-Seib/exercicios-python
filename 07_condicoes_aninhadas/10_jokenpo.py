from random import randint
from time import sleep

itens = ["Pedra", "Papel", "Tesoura"]
maq = randint(0,2)

print("""SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")

jogador = int(input("Qual a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")

print("-=" * 12)
print(f"Computador jogou {itens[maq]}")
print(f"Jogador jogou {itens[jogador]}")
print("-=" * 12)

if maq == 0: # maquina jogou PEDRA
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVÁLIDA!")
elif maq == 1: # maquina jogou PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVÁLIDA!")
elif maq == 2: # maquina jogou TESOURA
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA!")