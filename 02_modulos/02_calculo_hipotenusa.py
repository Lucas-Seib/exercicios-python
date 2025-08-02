from math import hypot

co = float(input("Medida do cateto oposto: "))
ca = float(input("Medida do cateto adjacente: "))

hi = hypot(ca, co)

print(f"O comprimento da hipotenusa é: {hi:.2f}")