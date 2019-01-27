n=int(input())
a=[]
while n>0:
	d=n%10
	#print(d)
	n=n//10
	a.append(d)
print(a)
for i in range(0,len(a)):
	for j in range(1,len(a)):
		if a[i]==a[j]:
			print("yes")
		
	break
