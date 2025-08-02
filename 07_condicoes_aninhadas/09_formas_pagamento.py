preco_real = float(input("Digite o preço do produto: R$"))

print("""FORMAS DE PAGAMENTO
[1] a vista dinheiro/cheque (desconto 10%)
[2] a vista cartão          (desconto 5%)
[3] 2x no cartão            
[4] 3x ou mais no cartão    (juros de 20%)""")

opcao = int(input("Sua opção: "))

avista = preco_real - (preco_real*0.1)
cartao1x = preco_real - (preco_real*0.05)
cartao2x = preco_real
cartao3x = preco_real + (preco_real*2)

if opcao == 1:
    print(f"A vista recebe 10% de desconto, o preço de R${preco_real:.2f} foi para R${avista:.2f}")
elif opcao == 2:
    print(f"A vista no cartão recebe 5% de desconto, o preço de R${preco_real:.2f} foi para R${cartao1x:.2f}")
elif opcao == 3:
    print(f"Pagando em 2x o preço será R${cartao2x}")
elif opcao == 4:
    print(f"Pagando em 3x ou mais, o preço de R${preco_real:.2f} será de R${cartao3x:.2f}")
