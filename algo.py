#algoritmo 1783
import time
ano = input("digite o ano") #1783
l = int(len(ano)/2) #
a,b = ano[:l],ano[l:] #a = 17 b=83
l2 = int(len(b)/2) 
c,d = b[:l2],b[l2:] #c = 8 d = 3
#print(d) #
sobraano = int(a)%4 #17%4 = 1 sobra
e = int(d) - sobraano
f = 2*e
g = int(b)/12
print(int(g))
h = int(b)%12
print(int(h))
