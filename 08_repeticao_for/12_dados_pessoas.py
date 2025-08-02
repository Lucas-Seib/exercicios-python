somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ""
totmulher20 = 0

for p in range(1, 5):
    print(f"----- {p}ª PESSOA -----")
    nome = str(input("Nome: ")).strip().capitalize()
    idade = int(input("Idade "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()
    somaidade = somaidade + idade
    if p == 1 and sexo in "M":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "M" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "F" and idade < 20:
        totmulher20 += 1


mediaidade = somaidade / 4
print(f"A média de idade do grupo é de {mediaidade:.2f} anos")
print(f"O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}")
print(f"Ao todo são {totmulher20} mulheres com menos de 20 anos")
