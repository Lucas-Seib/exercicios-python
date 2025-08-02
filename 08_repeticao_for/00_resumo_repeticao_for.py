# CTRL + K + CTRL + C = DEIXA TUDO EM COMENTARIO
# CTRL + K + CTRL + U = TIRA O COMENTARIO

# REPETIÇÃO FOR

for c in range(0,6): # O último numero ele ignora, então pra contar de 0 até 5, precisa colocar 0,6, se quiser de 1 a 6, seria 1,7
    print(c)         # se quiser que considere o ultimo numero pode colocar +1 no final
print("FIM")

# # REPETIR DE TRÁS PRA FRENTE
for c in range(6, 0, -1): # basta colocar o -1 no final, se quiser que diminua de 2 em 2, coloque -2
    print(c)

# # PULAR REPETIÇÃO
for c in range(0, 7, 2): # O 2 representa o numero de casas que vai pular, aqui fica 0 2 4 6
    print(c)

i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

for c in range(i, f+1, p):
    print(c)
print("FIM")

# INPUT DENTRO DO FOR COM SOMA DE CADA UM
s = 0
for c in range(0, 4):
    n = int(input("Digite um valor: "))
    s += n       # significa s = s + n
print(f"O somatorio de todos os valores foi {s}")