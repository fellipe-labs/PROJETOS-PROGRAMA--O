# Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
try:
    quant = int(input("Insira o número de pessoas: (7)"))
    cont1 = 0
    cont2 = 0
    for i in range(0, quant):
        data = int(input("Insira a data de nascimento da {}° pessoa: ".format(i+1)))
        if 2025 - data >= 18:
            cont1 = cont1 + 1
        elif 2025 - data <= 18:
            cont2 = cont2 +1
    print("""Ao todo, tivemos {} pessoas maiores de idade
E tivemos {} pessoas menores de idade""".format(cont1, cont2))
except ValueError:
    print("Insira um valor válido!")