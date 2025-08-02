r1 = float(input("Digite o primeiro comprimento: "))
r2 = float(input("Digite o segundo comprimento: "))
r3 = float(input("Digite o terceiro comprimento: "))

if r1<r2+r3 and r2<r3+r1 and r3<r1+r2:
    print("É possível formar um triangulo com estas medidas!")
else:
    print("Não é possível formar um triangulo.")