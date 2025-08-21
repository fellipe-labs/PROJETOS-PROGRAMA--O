sentence = str(input("Digite uma frase:  ")).upper()
print("""A letra A aparece {} vezes
A letra A aparece pela primeira vez em {}
A letra A aparece pela última vez em {}""".format(
sentence.count("A"), sentence.find("A"), sentence.rfind("A")))