

# Find cube of a perfect cube number

x = int(input("Enter the number :  "))

ans = 0

for i in range(0, abs(x)+1):

    if ans**3 >= abs(x):
        break
    else:
        ans += 1

if ans**3 != abs(x):

    print("Your number is not a perfect cube .")

else:

    if x < 0:
        ans = - ans

    print("cube of the number {} is {} .".format(x, ans))

