soma = 0
contador = 0

for c in range(1, 7):
    num = int(input(f"Digite o {c} valor: "))
    if num % 2 == 0:
        soma = soma + num
        contador = contador + 1

print(f"Você informou {contador} números PARES e a soma foi {soma}")
