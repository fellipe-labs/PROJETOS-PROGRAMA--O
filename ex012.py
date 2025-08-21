prize = float(input())
discount = int(input())
off = prize * (discount/100)
print("Com o desconto, o valor ficará R${}".format(prize - off))