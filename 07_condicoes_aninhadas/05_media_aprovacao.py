n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

media = (n1+n2)/2

if media < 5.0:
    print(f"Como sua média é {media:.1f}, você foi REPROVADO!")
elif 5.0 < media < 6.9:
    print(f"Como sua média é {media:.1f}, você está de RECUPERAÇÃO")
else:
    print(f"Como sua média é {media:.1f}, você foi APROVADO!")