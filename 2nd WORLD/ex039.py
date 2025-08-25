y = int(input('Qual seu ano de nascimento? '))
idade = 2025 - y
print("Quem nasceu em {} tem {} anos em 2025".format(y, 2025 - y))
if idade < 18:
    print("""Ainda faltam {} anos pro seu alistamento
Seu alistamento será em {}""".format(18 - idade, y + 18))
elif idade > 18:
    print("""Você já deveria ter se alistado há {} anos
Seu alistamento foi em {}""".format((idade - 18), y + 18))
else:
    print("Você tem que se alistar IMEDIATAMENTE")
