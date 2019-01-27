n,k=input().split()
a=int(k)
print(a,n)
print(n[0])
for i in range(0,len(n)):
	if n[i]>=0 and n[i]<=k:
		print("yes")
	else:
		print("no")
