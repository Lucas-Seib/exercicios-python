# Utilizando módulos
 
# Bibliotecas:
# bebida: suco café leite
# comida: arroz pão ovo
# doce: bolo pudim sorvete

# Para importar a biblioteca inteira:

# import bebida

# Para importar um ou mais itens da biblioteca:

# from doce import pudim
# from doce import púdim,bolo

# Biblioteca de matemática com funções extras: math
# exemplos de funcionalidades da biblioteca math

# ceil = arredonda o valor para cima
# floor = arredonda o valor para baixo
# trunc = elimina o número da vírgula para frente
# pow = potencia, semelhante a **
# sqrt = raiz quadrada
# factorial = fatorial

from math import sqrt
# numero = int(input("Digite um número: "))

# raiz = sqrt(numero)

# print(f"A raiz de {numero} é igual a {raiz:.2f}")

# Biblioteca que gera números aleatórios: random 

import random
num = random.random() # o metodo random da classe random gera um número float entre 0 e 1
numint = random.randint(1, 10) # randint gera numeros inteiros, nesse caso de 1 a 10

print(numint)