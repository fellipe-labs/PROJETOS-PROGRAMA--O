#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

try:
    num = int(input("Insira o número: "))
    s = 0
    cont = 0
    for i in range(1, num+1):
        if num % i == 0:
            cont = cont + 1
    if cont <= 2:
        print("O número É primo")
    if cont >= 3:
        print("O número NÃO é primo porque é divisível por {} números diferentes".format(cont))
except ValueError:
    print("Insira um número válido!")