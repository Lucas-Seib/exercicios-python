from random import choice

n1 = input("Nome 1: ")
n2 = input("Nome 2: ")
n3 = input("Nome 3: ")
n4 = input("Nome 4: ")

lista = [n1, n2, n3, n4]

sorteado = choice(lista)

print(f"O sorteado(a) foi {sorteado}")