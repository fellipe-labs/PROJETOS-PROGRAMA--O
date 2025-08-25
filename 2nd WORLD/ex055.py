#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

try:
    quant = int(input("Insira o número de pessoas: (5)"))
    maior = 0
    menor = 0
    for i in range(0, quant):
        peso = float(input("Insira o peso da {}° pessoa: ".format(i+1)))
        if i == 1:
            maior = peso
            menor = peso
        else:
            if peso > maior:
                maior = peso
            if peso < menor:
                menor = peso
    print("""O maior peso apresentado foi {}
    E o menor foi {}""".format(maior, menor))
except ValueError:
    print("insira um valor válido")

