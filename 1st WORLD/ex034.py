salary = float(input("Escreva aqui o seu salário: "))
ns = 1
if salary <= 1250:
    ns = (salary * 0.15) + salary
else:
    ns = (salary * 0.1) +salary
print('Seu novo salário será de R${}'.format(ns))