n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))

num = 0

while num != 5:
    print ("Escolha uma opção:\n[1] somar\n[2] multiplicar \n[3] maior\n[4] novos números\n[5] sair do programa")
    num = int(input("Qual é sua opção? "))
    
    soma = n1 + n2
    multi = n1 * n2
    maior = max (n1, n2)
    
    if num == 1:
        print(f"A soma dos valores {n1} e {n2} é: {soma}")
    elif num == 2:
        print(f"A multiplicação dos valores {n1} e {n2} é: {multi}")
    elif num == 3:
        print(f"O maior entre os valores {n1} e {n2} é: {maior}")
    elif num == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif num == 5:
        print("Saindo do programa...")
    else:
        print("Opção inválida, tente novamente!")
    print("=-=" * 15)
print("Programa finalizado, volte sempre!")
