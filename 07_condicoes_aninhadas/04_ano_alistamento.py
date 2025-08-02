from datetime import date

nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - nascimento

if idade < 18:
    print(f"Como você tem {idade} anos, ainda vai se alistar ao serviço militar.")
    print(f"Faltam {18 - idade} anos para se alistar.")
elif idade == 18:
    print(f"Como você tem {idade} anos, está na hora de se alistar!")
elif idade > 18:
    print(f"Como você tem {idade} anos, já passou do prazo para se alistar ao serviço militar.")
    print(f"Já se passaram {idade - 18} anos desde o prazo para de alistamento.")

