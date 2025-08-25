# O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no 
# peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o 
# indivíduo dentro de certas faixas. 
# abaixo de 18.5: Abaixo do peso 
# - entre 18.5 e 25: Peso ideal 
# - entre 25 e 30: Sobrepeso 
# - entre 30 e 40: Obesidade 
# - acima de 40: Obseidade mórbida 



try:    
    p = float(input("Insira seu peso: "))
    a = float(input("Insira sua altura: "))
    imc = p / a
    if imc < 18.5:
        print("Abaixo do peso")
    elif imc >= 18.5 and imc < 25:
        print("Peso ideal")
    elif imc >= 25 and imc < 30:
        print("Sobrepeso")
    elif imc >= 30 and imc < 40:
        print("Obesidade")
    elif imc >= 40:
        print("Obesidade mórbida")
except ValueError:
    print('Insira um valor válido')
