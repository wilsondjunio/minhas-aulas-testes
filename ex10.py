#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#considerando dolar 5.14

din=float(input("quanto dinheiro você tem na carteira? "))
res=din/5.14
print("com {} você pode comprar U${:.2f}".format(din,res))