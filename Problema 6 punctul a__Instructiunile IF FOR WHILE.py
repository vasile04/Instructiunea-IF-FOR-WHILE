s1=0
a=0
s2=0
n=eval(input('Introdu valoarea lui n: '))
for i in (1, (n+1)):
    s1+=i**3
    a+=i
    s2+=a**2
if s1<s2:
    print(s1, '<', s2)
else:
    print(s1, '>', s2)