name = str(input("Qual seu nome completo?  ")).strip()
nickname = name.split()

print("""Seu primeiro nome é: {}
Seu último nome é: {}""".format(nickname[0], nickname[len(nickname)-1]))