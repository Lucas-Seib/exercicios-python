
# Para começar uma config de cor para o texto, no padrão ANSI:
# \033[style;text;backm

# Para fechar a config:
# \033[m

# STYLE (forma da letra)

# 0 = Sem estilo
# 1 = Negrito
# 4 = Sublinhado
# 7 = Negativo (troca a config de letra para fundo ou de fundo para letra)

# TEXT (cor da letra)

# 30 = Cinza
# 31 = Vermelho
# 32 = Verde
# 33 = Amarelo
# 34 = Lilás
# 35 = Rosa
# 36 = Ciano
# 37 = Branco

# BACK (cor de fundo)

# 40 = Cinza
# 41 = Vermelho
# 42 = Verde
# 43 = Amarelo
# 44 = Lilás
# 45 = Rosa
# 46 = Ciano
# 47 = Branco

# OPÇÃO MAIS CONFUSA

a = 1
b = 2

print(f"os valores são \033[32m{a}\033[m e \033[31m{b}\033[m")

# OPÇÃO FORMATANDO AS CORES COM LISTA DENTRO DE UMA VARIAVAEL E O FECHADOR DE COR

nome = "Lucas"
cores = {"ciano":"\033[36m",
         "amarelo":"\033[33m",
         "vermelho":"\033[31m"}

fecha = "\033[m"

print(f"Prazer em te conhecer, {cores["vermelho"]}{nome}{fecha}")


print ("=# * 20")