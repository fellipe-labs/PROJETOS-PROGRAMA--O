year = int(input('Insira o ano: '))
b = year % 4
if b == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')