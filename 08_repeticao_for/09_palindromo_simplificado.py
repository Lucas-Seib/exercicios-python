frase = str(input("Digite uma frase: ")).strip().upper() # leu a frase
palavras = frase.split() # splitou para que gere uma lista da frase separada
junto = "".join(palavras) # deixa sem nada entre as aspas para tirar os espaços, se quiser adc 1 espaço ou caractere para separar, só colocar entre as aspas. Aqui juntei tudo em uma string só

inverso = junto[::-1]
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("Temos um palindromo!")
else:
    print("A frase digitada não é um palindromo.")