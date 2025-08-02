dis = float(input("Digite a distancia da viagem em Km: "))

curt = 0.5 * 1

long = 0.45 * 1

if dis <= 200:
    print(f"O valor da passagem será: R${dis*curt:.2f}")
else:
    print(f"O valor da passagem será: R${dis*long:.2f}")