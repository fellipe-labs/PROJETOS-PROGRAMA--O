# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
contagem = 0
for i in range(1, 500, 2):
    if i % 3 == 0:
        contagem = contagem + 1
        s += i
print("A soma dos {} valores é de {}".format(contagem, s))
        

