# your code goes here
a,b=input().split()
for i in range(0,len(a)+1):
	if a[i]==b:
		print(i+1)
		break
