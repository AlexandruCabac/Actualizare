y,x,s,p=[],[],0,1
with open('input.txt','r')as f:
    x.extend(f.readline().split())
    y.extend(f.readline().split())
for k in range(0, min(len(y), len(x))):
    y[k]=int(y[k])
    x[k]=int(x[k])
for i in range(0, min(len(y), len(x))):
    s=s+y[i]
    p=p*x[i]
with open('output.txt','w')as f:
    f.write("{1}{0}{2}{0}{3}{0}{4}".format('\n',x[0]+x[1]+x[2],s,p,abs(y[2])))