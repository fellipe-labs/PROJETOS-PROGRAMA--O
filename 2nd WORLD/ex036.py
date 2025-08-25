house = float(input("Qual o valor da casa? "))
salary = float(input("Qual seu salário? "))
anos = int(input(' Em quantos anos você vai pagar?'))
if house / (anos*12) > salary * 0.30:
    print('Empréstimo NEGADO')
else:
    print('Empréstimo APROVADO')
print('Para pagar uma casa de {} em {}, a prestação será de {:.2f}'.format(house, anos, house / (anos*12)))
