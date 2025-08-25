#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input("Digite a frase: ")).upper().strip()
separar = frase.split()
juntar = "".join(separar)
s = ""
for l in range(len(juntar) - 1, -1, -1):
    s += juntar[l]
if s == juntar:
    print("Temos um palíndromo")
else:
    print("Não temos um palíndromo")
print(s, juntar)