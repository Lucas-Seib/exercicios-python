vel = float(input("Velocidade do veículo: "))

multa = 7.00 * (vel-80)

if vel > 80:
    print("Você foi multado!")
    print(f"O valor da multa é de: R${multa:.2f}")
else:
    print("Você está dentro do limite de velocidade.")

