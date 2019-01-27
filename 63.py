n=int(input())
a=[int(i) for i in input().split()]
b=[int(j) for j in input().split()]
for n in range(0,len(a)):
	for m in range(0,len(b)):
		if a[n]==b[m]:
			print(a[n],end=" ")
