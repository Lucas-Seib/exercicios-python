
# CONDIÇÕES ANINHADAS

# if (se) elif (se não se) else (se não)
# elif pode ser usado quantas vezes precisar

nome = str(input("Qual é seu nome?: "))

if nome == "Lucas":
    print(f"Que nome bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("Esse nome é popular no Brasil")
elif nome in "Ana Cláudia Jéssica Juliana":
    print("Belo nome feminino")
else: 
    print(f"Seu nome é bem normal")
print(f"Tenha um bom dia, {nome}")
