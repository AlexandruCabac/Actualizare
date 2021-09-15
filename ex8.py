x,a,b,v=[],[],[],0
with open('input.txt','r')as f:
    x.extend(f.readline().split())
for i in range(0,len(x)):
    x[i]=int(x[i])
for k in range(0, len(x)):
    v=k+1
    if max(x)==x[k]:
        a.append(v)
    if min(x)==x[k]:
        b.append(v)   
a,b=str(a),str(b)
with open('output.txt','w')as f:
    f.write("{1}{0}{2}{0}{3}{0}{4}{0}{5}".format('\n',sum(x)/24,max(x),min(x),a[1:len(a)-1],b[1:len(b)-1]))