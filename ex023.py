num = int(input("Digite um número: "))
u = num % 10
d = (num % 100) // 10
c = (num % 1000) // 100
m = num // 1000
print("O valor da unidade é {}".format(u))
print("O valor da dezena é {}".format(d))
print("O valor da centena é {}".format(c))
print("O valor do milhar é {}".format(m))



