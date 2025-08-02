r1 = float(input("Digite o primeiro comprimento: "))
r2 = float(input("Digite o segundo comprimento: "))
r3 = float(input("Digite o terceiro comprimento: "))

if r1<r2+r3 and r2<r3+r1 and r3<r1+r2:
    print("É possível formar um triangulo com estas medidas!")

    if r1==r2==r3:
        print("Como as 3 medidas são iguais, o tipo é EQUILÁTERO")
    elif r1==r2 or r2==r3 or r3==r1:
        print("Como 2 medidas são iguais, o tipo é ISÓCELES")
    elif r1!=r2 and r2!=r3 and r3!=r1:
        print("Como as 3 medidas são diferentes, o tipo é ESCALENO")
else:
    print("Não é possível formar um triangulo.")