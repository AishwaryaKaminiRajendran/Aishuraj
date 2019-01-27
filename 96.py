n=int(input())
i=n
a=[]
while n>0:
	d=n%10
	#b.append(d)
	#print(d)
	n=n//10
a.append(d)
#print(a)
b=i%10
c=a[0]+b
print(c)
