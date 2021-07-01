n = int(input("Enter a number : "))

for i in range(n+1):
	k = n ^ i
	print(str(n)+"^"+str(i)+"="+str(k))
