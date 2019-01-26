# your code goes here
s=input()
for i in range(0,len(s)):
	if s[i].isupper():
		print(s[i].lower(),end="")
    else:
    	print(s[i].upper(),end="")
