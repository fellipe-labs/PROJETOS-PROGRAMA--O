y = int(input("Qual sua data de nascimento? "))
idade = 2025 - y
print("O atleta tem {} anos".format(idade))
if idade <= 9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("Classificação: JUNIOR")
elif idade <= 25:
    print("Classificação: SÊNIOR")
elif idade > 25:
    print("Classificação: MASTER")