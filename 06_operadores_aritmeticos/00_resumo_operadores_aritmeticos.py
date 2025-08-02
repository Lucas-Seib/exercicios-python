# Operadores Aritméticos (para números ou variáveis que contenham números)
# + adição
# - subtração
# * multiplicação
# / divisão
# ** potência
# // divisão inteira (o numero que foi usado pra achar o resto da divisão, ex: 5/2, coloca o 2 em baixo pra multiplicar e dar 4 pra sobrar 1. 2 é a divisão inteira)
# % resto da divisão (usando o exemplo a cima, 1 é o resto da divisão)

# Ordem de Precedência
# 1 -> ()
# 2 -> **
# 3 -> * , / , // , %
# 4 -> + , -

# exemplo:
# 5 + 3 * 2 = 11
# 3 * 5 + 4 ** 2 = 31
# 3 * (5+4) ** 2 = 243
# 81**(1/2) = 9 (potencia de 1/2 significa raiz quadrada)
# 16**(1/3) = 2 (potencia de 1/3 significa raiz cúbica)

n1 = int(input("Primeiro valor: R$"))
n2 = int(input("Segundo valor: R$"))

soma = n1 + n2
mult = n1 * n2
div = n1 / n2
div_int = n1 // n2
pot = n1 ** n2

print(f"A soma é {soma}, \n o produto é {mult} \n e a divisão é {div:.2f}", end=" ") # end=" " faz o próximo print ser exibido no final do primeiro print
print(f"Divisão inteira é {div_int} e potencia é {pot}")                             # \n faz o texto quebrar para a próxima linha
