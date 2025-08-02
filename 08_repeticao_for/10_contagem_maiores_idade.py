from datetime import date

atual = date.today().year
totalmaior = 0
totalmenor = 0

for pessoas in range(1, 8):
    nasc = int(input(f"Em que ano a {pessoas} pessoa nasceu? "))
    idade = atual - nasc
    if idade >= 18:
        totalmaior = totalmaior + 1
    else:
        totalmenor = totalmenor + 1

print(f"Ao todo tivemos {totalmaior} pessoas maiores de idade")
print(f"E também tivemos {totalmenor} pessaos menores de idade")