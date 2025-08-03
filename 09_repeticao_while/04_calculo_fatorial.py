num = int(input("Digite um número para calcular seu fatorial: "))

contador = num 
fatorial = 1

print (f"Calculando {num}!")

while contador > 0:  # enquanto o contador for maior do que 0
    print(f"{contador}", end='')  # end='' para mostrar o resultado na mesma linha, sem paragrafo
    print(" x " if contador > 1 else " = ", end= '') # mostre x se o contador for maior que 1, caso contrário mostre =
    fatorial = fatorial * contador
    contador = contador - 1 # -1 vai tirar 1 do numero escolhido

print(f"{fatorial}")



    
