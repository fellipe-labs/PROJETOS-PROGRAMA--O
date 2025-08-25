# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.

print("""=======================================
=======================================
      PROGRESSÃO ARITMÉTICA
=======================================
=======================================""")
try:
    fst = int(input("Primeiro valor: "))
    scd = int(input("Razão: "))
    for i in range(fst,scd * 10, scd):
        print ("{} ".format(i), end="--> ")
    print("ACABOU")
except ValueError:
    print("Insira um número válido!")
    
