print()
print("CALCULADORA DE DESCONTO")
print()
preco_atual = float(input("Digite o preço do produto: "))

desconto = preco_atual * 0.15 # 15%
novo_valor = preco_atual - desconto

print()
print("Você ganhou 15% de desconto!!!")
print(f"O novo valor é de R${novo_valor:.2f}")
print()