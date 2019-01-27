n,k=map(int,input().split())
a=[int(i) for i in input().split()]
b=[]
for j in range(0,len(a)):
	if a[j]<k:
		b.append(a[j])
#c=sort(b)
		
print(b)
c=sort(b)
print(c)
