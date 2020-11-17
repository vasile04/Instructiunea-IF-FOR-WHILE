n=eval(input('Introdu n: '))
s1=0
s2=0
a1=0
a2=0
for i in range (1, (n+1)):
    a1+=(i**2)
    s1+=3*a1
    a2+=i
    s2=n**3+n**2+a2
if s1>s2:
    print(s1, '>', s2)
if s2>s1:
    print(s2, '>', s1)
if s2==s1:
    print(s2, '=', s1)