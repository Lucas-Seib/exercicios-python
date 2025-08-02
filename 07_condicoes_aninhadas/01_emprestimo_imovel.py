casa = float(input("Valor da casa: R$ "))
sal = float(input("Valor do salário: R$"))
anos = int(input("Quantidade de anos que deseja pagar: "))

mensalidade = casa / (anos * 12)
minimo = sal * 30 / 100

print(f"Para pagar uma casa no valor de R${casa:.2f} em {anos} anos, a prestação será de R${mensalidade:.2f}.")

if mensalidade >= minimo:
    print("Empréstimo NEGADO!")
else:
    print("Empréstimo AUTORIZADO!")