# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

print("======== LOJAS FELPS =======")
v = float(input("Valor das compras: "))
f = int(input("""FORMA DE PAGAMENTO
[ 1 ] à vista no dinheiro/cheque: 10% de desconto
[ 2 ] à vista no cartão: 5% de desconto
[ 3 ] em até 2x no cartão: preço formal
[ 4 ] 3x ou mais no cartão: 20% de juros
Qual a opção? """))
while f not in (1, 2, 3, 4):
    print("Insira um valor válido!")
    f = int(input("""FORMA DE PAGAMENTO
    [ 1 ] à vista no dinheiro/cheque: 10% de desconto
    [ 2 ] à vista no cartão: 5% de desconto
    [ 3 ] em até 2x no cartão: preço formal
    [ 4 ] 3x ou mais no cartão: 20% de juros
    Qual a opção? """))
if f == 1:
    print("Seu produto de valor {} custará {} no final".format(v, v - (v * 0.1)))
elif f == 2:
    print("Seu produto de valor {} custará {} no final".format(v, v - (v * 0.05)))
elif f == 3:
    print("Seu produto de valor {} custará {} em 2x".format(v, v/2))
elif f == 4:
    valor = v + (v * 0.2)
    p = int(input("Deseja parcelar em quantas x? "))
    print("Seu produto de valor {} custará {} em {}x".format(valor, valor/p, p))

