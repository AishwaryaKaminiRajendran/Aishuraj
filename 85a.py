n=input()
x=' '
y=' '
for i in range(0,len(n)):
	if i%2==0:
		x=x+n[i]
print(x.strip(),end=" ")
for j in range(0,len(n)):
	if j%2==1:
		y=y+n[j]
print(y.strip())
