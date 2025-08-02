# Manipulando Cadeias de Texto

# frase =
# |C|u|r|s|o| |e|m| |V|i |d |e |o |  |P |y |t |h |o |n |
# |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|

# **Fatiamento**

# frase[9:13] vai puxar a parte "Vide" pq não pega a ultima letra, caso queira a letra "o" o codigo fica [9:14]
# frase[9:21] vai puxar até a ultima letra, já que o 21 não existe (mas existe forma mais fácil do que colocar uma casa q não existe)

# frase[9:21:2] vai da casa 9 até a 21(20), mas saltando de 2 em 2 "V d o P t o"

# frase[:5] quando nao tem valor antes do sinal : é como se escrevesse "0:" e vai puxar do início até a casa 5 do exemplo "C u r s o"
# frase[15:] o contrário do exemplo anterior, mostrando da casa até o fim da frase (essa é a forma mais inteligente do exemplo 2) "P y t h o n"

# frase[9::3] 9: vai da casa 9 até o fim | :3 vai pular 3 casas até o fim "V e P h"
 

# **Análise**

# len = significa "comprimento"
# len(frase) = 21 caracteres

# count = signifca "contar"
# frase.count("o") = conta quantas vezes a letra "o" aparece na variável frase, nesse caso vai dar 3
# frase.count("o",0,13) = vai contar quantas vezes a letra aparece do caractere 0 até o 13, nesse caso vai dar 1

# find = significa "encontrar"
# frase.find("deo") = vai mostrar a casa onde encontrou/iniciou a letra ou palavra na frase, nesse caso encontrou "deo" na casa 11
# frase.find("Android") = quando a string não existir dentro da minha string vai me retornar "-1" pq Android não existe na frase

# in = operador que significa "Existe em"
# "Curso" in frase =  "Curso existe em frase"


# **Transformação**

# replace = significa "trocar/reposicionar"
# frase.replace("Python","Android") = vai substituir "Python" por "Android"

# upper = significa "para cima/MAIÚSCULA"
# o que já for maiúscula ele mantém, o que não for ele altera
# frase.upper()

# lower = significa "baixo/minúscula"
# o que já for minúscula ele mantém, o que não for ele altera
# frase.lower()

# capitalize = muda a primeira letra para maiúscula e todo o restante para minúscula
# frase.capitalize()

# title = muda a primeira letra de cada palavra para maiúscula (analisa onde tem espaços)
# frase.title()


# frase =
# | | | |A|p|r|e|n|d|a|  |P |y |t |h |o |n |  |  |
# |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|

# strip = remove todos os espaços no início e no final da string
# frase.strip()

# colocando "r" de right na frente para começar a tratar pela direita
# frase.rstrip() = remove só os últimos espaços da direita

# colocando "l" de left na frente para começar a tratar pela esquerda
# frase.lstrip() = remove só os primeiros espaços da esquerda


# **Divisão**

# frase.split() = cria uma divisão onde tem espaços dentro da string, com uma nova indexação
# E cada divisão se torna uma lista, cada uma com sua numeração (splitado)
# para selecionar cada pedaço escreva:
# print(dividido[1][3]) = "em Python"

# ex:
# |C|u|r|s|o| |e|m| |V|i|d|e|o| |P|y|t|h|o|n|
# |0|1|2|3|4| |0|1| |0|1|3|4|5| |0|1|2|3|4|5|
#      0        1        2            3

# análogo ao split, temos o join
# "-".join(frase) = junta todos os elementos de frase, mas dessa vez no lugar do espaço, entra um sinal de "-"
# caso eu queira que seja separado por espaço é só colocar () sem nada dentro

# ex:
# |C|u|r|s|o|-|e|m|-|V|i |d |e |o |- |P |y |t |h |o |n |
# |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|


# printar um texto com várias linhas usando """ 3 aspas

# ex:
# print("""flksdfskhfgkhsglçkfshgs
# lgsfkgslkfgçsflkgjsflkgjfsgfsgsf
# lskhglsfkglsfkghlsfkghsfdfsgfsgsf
# glsfkgçlsfkhglsfçkhgçsflkghsflçgl""")

frase = "Curso em Video Python"
print(frase.upper().count("O")) # coloquei todas pra maiuscula e contei qnts O tem nela

frase2 = "Aprenda Python"
frase2 = frase2.replace("Python","Jorginho") # troquei uma palavra pela outra
print(frase2)

frase3 = "Curso para Gafanhotos"
print(frase3.lower().find("gafanhotos")) # diminuí com lower todas as letras da frase e procurei o termo gafanhotos minusculo
#                                          me retornou a casa 11 que é onde começa a palavra "gafanhotos"
