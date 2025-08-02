num = int(input("Digite o número a ser convertido: "))
print("""Escolha a base de conversão: 
1 = BINARIO 
2 = OCTAL  
3 = HEXADECIMAL""")
opcao = int(input("Sua opção: "))

n1 = bin(num)
n2 = oct(num)
n3 = hex(num)

if opcao == 1:
    print(f"A conversão do número {num} para BINÁRIO é {n1[2:]}")
elif opcao == 2:
    print(f"A conversão do número {num} para OCTAL é {n2[2:]}")
elif opcao == 3:
    print(f"A conversão do número {num} para HEXADECIMAL é {n3[2:]}")
else:
    print("Opção inválida, tente novamente!")