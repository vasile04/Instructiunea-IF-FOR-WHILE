n=int(input("introduceti varsta lui Mihai: "))
a=1
if n<20:    
    for i in range(1,n+1):
        if (i==1):
            a=a+2
        else:
            a=(a*2)+i
print("La varsta de",n,"ani Mihai a primit:",a,"$")
print("Cadoul lui Mihai a fost mai mare de 100$ la 6 ani")