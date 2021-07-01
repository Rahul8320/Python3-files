print("Welcome to The Collatz Sequence ..Have Fun !!!")

def collatz(num):
	if num%2==0:
		num = num // 2
		print(num)
		return num
	else:
		num = 3*num + 1
		print(num)
		return num
		
def main():
	n = int(input("Enter Number >>> "))
	print(n)
	while True:
		n = collatz(n)
		if n==1:
			break
			 
main()

