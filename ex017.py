import math
CO = float(input("Digite o cateto oposto: "))
CA = float(input("Digite o cateto adjacente: "))
H = math.sqrt((CO ** 2) + (CA ** 2))
print("O cateto oposto é {}, o adjacente é {} e a hipotenusa é {}".format(CO, CA, H))
