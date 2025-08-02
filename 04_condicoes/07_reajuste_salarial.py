salario = float(input("Digite o valor do salário: "))

sup = salario * 0.1

inf = salario * 0.15

salario2 = salario+sup
salario3 = salario+inf

if salario > 1250:
    print(f"Como seu salário é SUPERIOR a R$1250, seu aumento será de R${sup}, atualizando para R${salario2}")
else:
    print(f"Como seu salário é INFERIOR a R$1250, seu aumento será de R${inf}, atualizando para R${salario3}")