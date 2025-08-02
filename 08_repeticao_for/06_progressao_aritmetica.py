primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro + (10 - 1) * razao # formula para o décimo termo de uma PA, se fosse vigesimo seria 20

for c in range(primeiro, decimo + razao, razao):
    print(f"{c}", end=" ~ ")
print("ACABOU")