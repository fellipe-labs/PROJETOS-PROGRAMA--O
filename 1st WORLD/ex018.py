import math 

angulo = float(input("Digite o ângulo: "))
rad = math.radians(angulo)
sen = math.sen(rad)
cos = math.cos(rad)
print("Sendo o ângulo {}º, em radiano fica {}; seu seno é {} e seu cosseno é {}".format(angulo, rad, sen, cos))
