n1 = int(input("Escreva o número 1: "))
n2 = int(input("Escreva o número 2: "))
n3 = int(input("Escreva o número 3: "))
s = n1
if n2 < n1 and n2 < n3:
    s = n2
if n3 < n1 and n3 < n2:
    s = n3
b = n1
if n2 > n1 and n2 > n3:
    b = n2
if n3 > n1 and n3 > n2:
    b = n3

print('''O menor valor é {}
O maior valor é {}'''.format(s, b))