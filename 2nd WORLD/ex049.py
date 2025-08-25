#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
#só que agora utilizando um laço for.
try: 
    num = int(input("Insira o número a ser multiplicado: "))
    for i in range(1,11):
        print(num, " X ", i, " = ", num * i)
except ValueError:
    print('Insira um número Válido!')