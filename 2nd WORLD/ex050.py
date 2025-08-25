#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.

num = 1
s = 0
try:
    for i in range(0,6):
        num = int(input("Insira um número: "))
        if num % 2 == 0:
            s += num
    print("A soma dos valores pares dá {}".format(s))
except ValueError:
    print("Insira um número válido!")