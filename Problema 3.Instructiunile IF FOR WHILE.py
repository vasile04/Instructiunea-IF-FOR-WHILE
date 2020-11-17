# Se dau numerele m si n, unde m<n. Sa se verifice daca n este o putere a lui m
from math import log
m=int(input('Introdu valoarea lui m:'))
n=int(input('Introdu valoarea lui n:'))
a=log(n, m)
l=int(a)
if a-l==0:
    print ("n este putere al lui m")
else:
    print("n nu este putere al lui m")