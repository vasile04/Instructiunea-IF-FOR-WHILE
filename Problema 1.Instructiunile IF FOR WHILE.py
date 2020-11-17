# Se dă numarul natural n n={28, 29, 30, 31}. Sa se afișeze lunile cu numărul n de zile 
n=int(input('Introduceți numărul de zile ale lunii: '))
if (n==28) and (n==29):
    print('Luna cu', n , 'de zile este februarie' )

if n==30:
    print('Lunile cu', n , 'de zile sunt aprilie, iunie, septembrie, noiembrie')

if n==31:
    print('Lunile cu', n , 'de zile sunt ianuarie, martie, mai, iulie, august, octombrie, decembrie')

if n<28 or n>31:
    print('Luna cu ', n , 'de zile nu există' )