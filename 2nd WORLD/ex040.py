n1 = float(input("Nota 1 : "))
n2 = float(input("Nota 2 : "))
med = (n1 + n2) / 2
if med >= 7:
    print("Parabéns, você obteve média {:.1f} e está APROVADO".format(med))
elif med < 7 and med >= 5:
    print("Você obteve média {} e está de RECUPERAÇÃO".format(med))
else:
    print("Você obteve média {} e está REPROVADO".format(med))
    
