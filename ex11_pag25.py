def verificare(q):
    w=0
    for u in range(1,q):
        if(q%u==0):
            w+=1
    return w
import string
NO,l,b,d,nr,e,f1,g,h,d1,b1='Nu_sunt',[],[],[],[],[],[],[],[],[],[]
with open('input.txt','r')as f:
    n=f.readline()
    if(int(n)<10):
        l.extend(f.readline().split())
        nr.extend(f.readlines())
        nr[0]=nr[0][:len(nr[0])-1]
        l,nr=list(map(int,l)),list(map(int,nr))
        a=str(list(reversed(l)))
        c=str(sorted(l,reverse=True))
        for k in range(0,len(l)):
            if(l[k]%2==0):
                b.append(l[k])
                b1.append(l[k])
            else:
                d.append(l[k])
                d1.append(l[k])
                if(l[k]<0):
                    g.append(k)
                else:
                    g.append(NO) 
            if(l[k]>nr[0] and l[k]%nr[1]!=0):
                e.append(l[k])
            else:
                e.append(NO)
            if(l[k]>nr[0] and l[k]<nr[1]):
                f1.append(l[k])
            else:
                f1.append(NO)
            if(l[k]>9 and l[k]<100):
                h.append(k)
            else:
                h.append(NO)
        if(len(b)==0):
            s='Nu sunt numere pare'
            b.append(NO)
        else:
            s=sum(b)/len(b)
        if(len(d)==0):
            d.append(NO)
            d1.append(NO)
        b,d,e,f1,g,h=str(b),str(d),str(e),str(f1),str(g),str(h)
        b,d=b[1:len(b)-1],d[1:len(d)-1]
        with open('output.txt','w')as f:
            n=[]
            f.write("{0}{1}".format("Afiseaza pe ecran componentele tabloului la un interval de 5 pozitii:",'\n'))
            for i in range(0,len(l)):
                f.write('%5d'%(l[i]))
                n.append(l[i])
            nr[0],nr[1]=l[0],n.index(min(n))
            n[0]=min(n)
            n=str(n)
            f.write("{0}{1}{0}{2}".format('\n',"Afiseaza pe ecran numerele in ordinea inversa a introducerii in calculator:",a[1:len(a)-1]))
            f.write("{0}{1}{0}{2}".format('\n',"Sorteaza componentele tabloului in ordine descrescatoare:",c[1:len(c)-1]))
            f.write("{0}{1}{0}{2}".format('\n',"Afiseaza pe ecran doar componentele pare:",b[1:len(b)-1]))
            f.write("{0}{1}{0}{2}".format('\n',"Afiseaza pe ecran media aritmetica a componentelor pare:",str(s)))
            f.write("{0}{1}{0}{2}".format('\n',"Afiseaza pe ecran doar componentele impare:",d[1:len(d)-1]))
            f.write("{0}{1}{0}{2}".format('\n',"Afiseaza pe ecran doar componentele care sunt mai mari ca x si nu sunt divizibile cu y:",e[1:len(e)-1]))
            f.write("{0}{1}{0}{2}".format('\n',"Afiseaza pe ecran doar componentele care sunt mai mari ca x si mai mici decat y:",f1[1:len(f1)-1]))
            f.write("{0}{1}{0}{2}".format('\n',"Afiseaza pe ecran pozitiile (indicii) componentelor impare negative:",g[1:len(g)-1]))
            f.write("{0}{1}{0}{2}".format('\n',"Afiseaza pe ecran pozitiile (indicii) componentelor ce contin doar doua cifre semnificative:",h[1:len(h)-1]))
            f.write("{0}{1}{0}{2}".format('\n',"Inlocuieste prima componenta a tabloului cu componenta de valoare minima din tabloul respectiv:",n[1:len(n)-1]))
            n=list(n.split())
            n[0],n[nr[1]]=nr[0],nr[0]
            n=str(n)
            f.write("{0}{1}{0}{2}".format('\n',"Inlocuieste componenta de valoare minima din tabloul respectiv cu prima componenta a acestuia:",n[1:len(n)-1]))
            f.write("{0}{1}{0}{2}".format('\n',"Creeaza un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatura:",str(b1)))
            if(d1[0]!=NO):
                z=0
                while(len(d1)>z):
                    if(d1[z]%3!=0):
                        d1.pop(z)
                        z-=1
                    z+=1
            f.write("{0}{1}{0}{2}".format('\n',"Creeaza un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatura:",str(d1)))
            l=list(map(verificare,l))
            for z in range(0, len(l)):
                if(l[z]>4):
                    l.pop(z)
            if(len(l)!=0):
                l=str(l)
            else:
                l.append(NO)
            f.write("{0}{1}{0}{2}".format('\n',"Creeaza un tablou nou, format doar din acele componente ale tabloului introdus de la tastatura care au cel mult patru divizori:",l[1:len(l)-1]))
    else:
        with open('output.txt','w')as f:
            f.write("Prea multe valori")