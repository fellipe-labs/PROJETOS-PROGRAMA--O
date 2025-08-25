num = int(input("Escreva a distância da sua viagem: "))
if num <= 200:
    print("O preço da passagem será R${}".format(num * 0.5))
else:
    print('O preço da sua passagem será de R${}'.format(num * 0.45))
