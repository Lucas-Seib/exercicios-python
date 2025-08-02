print()
print("CALCULADORA DE ÁREA E RENDIMENTO DE TINTA")
print()
largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))

area = largura * altura

# litro de tinta vale 2m2
rendimento = area / 2

print()
print(f"A área da parede é {area:.2f}m2")
print(f"Para pintar esta parede você precisará de {rendimento} litros de tinta")
print()