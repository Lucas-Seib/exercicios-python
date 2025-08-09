print("Sequência de Fibonacci")
print()
num = int(input("Quantos termos você quer mostrar? "))

t1 = 0
t2 = 1

print()
print(f"{t1} -> {t2}", end="") # end="" tira o paragrafo, deixando tudo na mesma linha

contador = 3 # contador começa em 3 porque ja foi mostrado o termo 1 e 2

while contador <= num:
    t3 = t1 + t2
    print(f" -> {t3}", end="")
    t1 = t2   # transforma o t1 em t2, fazendo com que sequencia de soma avance, dessa forma ele se tranforma no próximo e soma ao anterior
    t2 = t3   # transforma o t2 em t3, fazendo com que sequencia de soma avance, dessa forma ele se tranforma no próximo e soma ao anterior
    contador = contador + 1
print(" -> FIM")
