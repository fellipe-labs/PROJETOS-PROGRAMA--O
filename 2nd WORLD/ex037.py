num = int(input("Número a ser convertido: "))
conversão = int(input("""Qual o tipo de conversão?
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal ]"""))
if conversão == 1:
    print(bin(num))
elif conversão == 2:
    print(oct(num))
elif conversão == 3:
    print(hex(num))
else: 
    print("Esse tipo de conversão não existe!")