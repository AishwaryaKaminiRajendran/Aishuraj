a,b=map(int,input().split())
#print(a,b)
s=0
for i in range(a,b+1):
	if i%2!=0:
		s=s+i
print(s)
    
