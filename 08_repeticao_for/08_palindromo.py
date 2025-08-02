frase = str(input("Digite uma frase: ")).strip().upper() # leu a frase
palavras = frase.split() # splitou para que gere uma lista da frase separada
junto = "".join(palavras) # deixa sem nada entre as aspas para tirar os espaços, se quiser adc 1 espaço ou caractere para separar, só colocar entre as aspas. Aqui juntei tudo em uma string só
inverso = ""

for letra in range(len(junto) -1, -1, -1): # len(junto) ele pega o numero de letras do junto e tira 1, vai até a letra -1(antes da primeira que é 0) e o ultimo -1 diz que vai voltar 1 letra
    inverso = inverso + junto[letra]
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("Temos um palindromo!")
else:
    print("A frase digitada não é um palindromo.")
