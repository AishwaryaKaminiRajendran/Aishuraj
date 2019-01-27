n,k=map(int,input().split())
a=[int(i) for i in input().split()]
print(a)
print(k)
for n in range(0,len(a)):
	if a[n]-a[n+1]==1 or a[n]-a[n+1]==-1:
		print("g")
#for m in range(0,len(a)):
if a[n]==k:
	print(n+1)
			 
