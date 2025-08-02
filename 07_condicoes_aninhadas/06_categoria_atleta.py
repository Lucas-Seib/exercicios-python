from datetime import date

ano = int(input("Digite o ano de nascimento do atleta: "))

ano_atual = date.today().year
idade = ano_atual - ano

if idade <= 9:
    print(f"Como sua idade é de {idade} anos, sua categoria é: MIRIM")
elif idade <= 14:
    print(f"Como sua idade é de {idade} anos, sua categoria é: INFANTIL")
elif idade <= 19:
    print(f"Como sua idade é de {idade} anos, sua categoria é: JUNIOR")
elif idade == 20:
    print(f"Como sua idade é de {idade} anos, sua categoria é: SENIOR")
else:
    print(f"Como sua idade é de {idade} anos, sua categoria é: MASTER")