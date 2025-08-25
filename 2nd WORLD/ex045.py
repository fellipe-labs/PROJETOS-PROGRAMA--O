#Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
import random

jogadas = ["PEDRA", "PAPEL", "TESOURA"]
pc = random.choice(jogadas)
j = int(input("""
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
Qual vai ser sua jogada? """)) 
player = 0
while j not in(1, 2, 3):
    print("""
Jogada inválida. Tente novamente: """)
    j = int(input("""
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
Qual vai ser sua jogada? """))
if j == 1:
    player = "PEDRA"
elif j == 2:
    player = "PAPEL"
elif j == 3:
    player = "TESOURA"
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(0.5)
print("""===================J O K E N P O======0=============

O COMPUTADOR ESCOLHEU [ {} ]
VOCÊ ESCOLHEU [ {} ]""".format(pc, player))
if player == pc:
    print("EMPATE")
elif (player == "PEDRA" and pc == "PAPEL") or \
(player == "PAPEL" and pc == "TESOURA") or \
(player == "TESOURA" and pc == "PEDRA"):
    print("YOU LOSE!!!!!")
else: 
    print("YOU WON!!!!!")
    