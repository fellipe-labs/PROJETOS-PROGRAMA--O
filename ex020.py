import random 

a1 = str(input())
a2 = str(input())
a3 = str(input())
a4 = str(input())
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print("A ordem de apresentação será: {}".format(lista))