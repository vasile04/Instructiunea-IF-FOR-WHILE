# Sa se calculeze 1!+2!+3!+...+n!, unde n>1
n=int(input('Introdu valoarea lui n: '))
factorial = 1
while n>1:
    factorial *=n
    n-=1

print('Factorialul de la 1 la n =', factorial)