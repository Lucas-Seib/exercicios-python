peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

imc = peso / altura ** 2
imc = round(imc,1) # arredonda o valor de IMC para duas casas decimais

if imc < 18.5:
    print(f"Como seu IMC é {imc}, seu status é: ABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print(f"Como seu IMC é {imc}, seu status é: PESO IDEAL")
elif 25 <= imc < 30:
    print(f"Como seu IMC é {imc}, seu status é: SOBREPESO")
elif 30 <= imc < 40:
    print(f"Como seu IMC é {imc}, seu status é: OBESIDADE")
else:
    print(f"Como seu IMC é {imc}, seu status é: OBESIDADE MORBIDA")