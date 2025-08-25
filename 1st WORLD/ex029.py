vel = int(input('Qual a sua velocidade? '))
if vel >= 80:
    print("Você foi multado em R${}".format(7 * (vel-80)))
else:
    print('Você está com a velocidade correta')