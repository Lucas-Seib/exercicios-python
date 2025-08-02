soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
    print(c, end=" ")
print()
print(f"A soma de todos os {cont} valores multiplos de 3 entre 1 e 500 são {soma}")