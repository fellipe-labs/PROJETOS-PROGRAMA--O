name = str(input("Qual o seu nome completo? "))
location = (name.upper()).find("SILVA")
print("Seu nome tem Silva? {}".format(name.upper()[location:] == "SILVA"))

 