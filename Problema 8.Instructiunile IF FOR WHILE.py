a=int(input('introdu lungimea primei lature:'))
b=int(input('Introdu lungimea laturei a doua:'))
c=int(input('Introdu lungimea laturei a treia:')) 
if (a<b+c) and(b<a+c) and (c<b+a):
    print('exista triungi cu laturile date')
else:
    print ('nu exista triungi cu laturile date')
if a==b and a==c:
    print(a, '=', b, '=', c, 'triunghiul este echilateral' )
if a==b or a==c or b==c:
    print('triunghiul este isoscel') 
if a!=b and a!=c and b!=c:
    print('Triunghiul este scalen')   