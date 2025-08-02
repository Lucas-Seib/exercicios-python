# ESTRUTURA DE REPETIÇÃO WHILE

# estrutura FOR usamos quando sabemos quantas repetições queremos fazer
# estrutura WHILE significa "ENQUANTO não chegar o destino, siga repetindo"
# usamos quando não sabemos quantas vezes serão

# ENQUANTO não MAÇÃ  (significa "enquanto não for MAÇÃ, dou um passo, quando for MAÇÃ ele pega")
#   passo
# pega

# EXEMPLO QUANDO TIVER OBSTACULOS NO CAMINHO, USAMOS CONDIÇÕES PARA FAZER VERIFICAÇÕES DURANTE O LAÇO DE REPETIÇÃO

# ENQUANTO não MAÇÃ      while not maçã
#   SE chão                  if chão
#       passo
#   SE vazio
#       pula
#   SE moeda
#       pega
# pega

# EXEMPLO FOR E WHILE COM MESMO RESULTADO

# for c in range (1,10):                         c = 1
#     print (c)                                  while c < 10:
# print ("Fim")                                     print (c)
#                                                   c = c + 1
#                                                print("Fim")


n = 1 
par = impar = 0

while n != 0:                            # enquanto "n" for diferente de 0, repita o imput "n" a seguir
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print (f"Você digitou {par} números pares e {impar} números ímpares!")