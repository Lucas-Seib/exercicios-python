print()
print("CONVERSOR REAL PARA DÓLAR")
print()
valor = float(input("Valor a ser convertido: R$"))

dolar = 5.64

resultado = valor / dolar

print()
print(f"Cotação atual do dólar R${dolar}")
print()
print(f"O valor R${valor:.2f} equivale a US${resultado:.2f}")
print()