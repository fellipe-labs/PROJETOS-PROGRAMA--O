import random

num = int(input("Escreva um número de 0 a 5: "))
num2 = random.randint(0,5)
if num == num2:
    print('PARABENNSSS!! VOCÊ PENSOU O MESMO NÚMERO QUE EU ')
else:
    print('slk, muito burro')
print("escolhi {}".format(num2))