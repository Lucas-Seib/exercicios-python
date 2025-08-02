print()
print("CALCULADORA DE AUMENTO SALARIAL")
print()
salario_atual = float(input("Salário atual: "))

aumento = salario_atual * 0.10 # 10%
novo_salario = salario_atual + aumento

print()
print("Você recebeu um aumento de 10%!")
print(f"Seu novo salário é de R${novo_salario:.2f}")
print()