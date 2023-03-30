import math

n=int(input("digite um numero: "))
d= (n*2)
t= (n*3)
r= math.sqrt(n)
#print("o dobro de {} é: ".format(d))
#print('o triplo de {}'.format(t))
#print('a raiz quadrada de {} é: {} '.format(n,r))
print('o dobro de {} é {}. \no triplo de {} é {} \na raiz quadrada de {} é {:.2f} '.format(n,d,n,t,n,r))
#dica, para mudar de linha no mesmo testo, usar \n e para formatar as casas decimais, dentro do {;.2f},
# ou qunatas casas decimais forem necessarias