x,y=[],['Luni','Marti','Miercuri','Joi','Vineri','Sambata','Duminica']
with open('input.txt','r')as f:
    x.extend(f.readline().split())
for i in range(0,len(x)):
    x[i]=int(x[i])
a,b=y[x.index(max(x))],y[x.index(min(x))]
with open('output.txt','w')as f:
    f.write("{1}{0}{2}{0}{3}{0}{4}".format('\n',sum(x),sum(x)/7,a,b)) 