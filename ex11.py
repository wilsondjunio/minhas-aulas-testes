#faça um prog que leia a largura e altura de uma parede em metros, calcule sua area
# e a quantidade de tinta necessariaa para pintar sabendo que cada litro de tinta pinta uma area de 2m

larg=float(input("largura da parede: "))
alt=float(input("altura da parede: "))
area=larg*alt
tinta=area/2
print("sua parede tem a dimensão de {}x{} e sua area é de {:.2f}m².\nPara pintar essa parede, você precisará de {:.2f}L de tinta".format(larg,alt,area,tinta))