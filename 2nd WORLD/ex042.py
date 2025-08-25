import math

try:
    ca = float(input("Cateto adjacente: "))
    co = float(input("Cateto oposto: "))
    h = float(input("Hipotenusa: "))
    if ca + co > h and ca + h > co and co + h > ca:
        print("FORMA triângulo")
        if co == ca == h:
            print("Forma um triângulo EQUILÁTERO")
        elif ca == co or ca == h or co == h:
            print("Forma um triângulo ISÓSCELES")
        elif ca != co and ca != h and co != h:
            print("Forma um triângulo ESCALENO")
    else: 
        print("NÃO forma")
except ValueError:
    print("Insira um valor válido ")
