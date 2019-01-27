# your code goes here
n,b=map(int,input().split())
x=[int(i) for i in input().split()]
#print(x)
#print(sum(x))
#print(b)
if sum(x)==b:
	print("yes")
else:
	print("no")
