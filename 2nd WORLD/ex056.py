#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
#  qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
try:
    quant = int(input("Insira o número de pessoas"))
    mi = 0
    mv = ""
    mu = 0
    media = 0
    maior_idade = 0 
    menor_idade = 0
    cont = 0
    for i in range(0, quant):
        print("----- {}° PESSOA -----".format(i+1))
        nome = str(input("Nome: "))
        Idade = int(input("Idade: "))
        sexo = str(input("Sexo  [M/F]: ").upper())
        mi += Idade
        media = mi / quant
        if sexo == "M":
            if Idade > maior_idade:
                maior_idade = Idade
                mv = nome
        elif sexo == "F":
            if Idade < 20:
                cont = cont + 1
    print("""A média de idade do grupo é {:.1f}
A pessoa mais velha é {}
Há {} mulheres com menos de 20 anos""".format(media, mv, cont))
except ValueError:
    print("Insira um valor válido!")


