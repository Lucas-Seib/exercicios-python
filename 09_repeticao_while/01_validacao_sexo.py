s = ""

while s != "M" and s != "F":
    s = input(" Digite o sexo: ").upper()
    if s != "M" and s != "F":
        print("Sexo inválido, digite novamente!")
    
print (f"O sexo informado {s} foi registrado")
