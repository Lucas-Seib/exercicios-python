# CONDIÇÕES SIMPLES E COMPOSTAS

#nome = str(input("Qual é seu nome? "))

#if nome == "Lucas":
#    print("Que nome lindo você tem!")
#print(f"Bom dia, {nome}!")



n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1+n2)/2

print(f"A sua média foi {media:.2f}")

if media >= 6.0:
    print("Sua média foi boa! PARABÉNS!")
else:
    print("Sua média foi ruim! ESTUDE MAIS")