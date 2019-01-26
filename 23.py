n=int(input())
k=int(input())
o=[]
x=[]
h=" "
for i in range(0,len(n)):
	a=int(input())
	o=o.append(a)
for j in range(0,len(k)):
	b=int(input())
	x=x.append(b)
for t in range(0,len(k)):
	u=h.append(k[t])
	p=max(u)
print(p)
