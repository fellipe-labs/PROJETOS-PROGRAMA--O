#Crie um programa que leia o nome de uma cidade e diga se começa com Santo ou não
city = str(input("Digite o nome da cidade que você nasceu: ")).strip()
print(city[:5].upper() == 'SANTO')


