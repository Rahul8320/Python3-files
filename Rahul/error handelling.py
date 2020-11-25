
a = int(input("Enter a number :  "))

b = int(input("Enter another number :  "))

try:

    print("File Open ")
    print(a/b)
    k = int(input("Enter a integer :  "))
    print(k)

except ZeroDivisionError as e:
    print("**Hey user, enter a wrong input {} not possible **".format(e))

except ValueError as e:
    print("**Hey user, enter a wrong input ... {} **".format(e))

except Exception as e:
    print("Hey user,something went wrong ....", e)

finally:
    print("File closed ")


print("Bye Bye User !!")
