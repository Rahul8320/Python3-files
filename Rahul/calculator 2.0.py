

from calculator import *
import os
import time as tm

print(" Available function : \n 1. ADD  2. SUB  3. MUL  4. DIV  5. FACT  6. CUBE_ROOT  7. SQ_ROOT 8. NTH_ROOT ")

print(" 9. SQR  10. CUBE  11. NTH_SQ  12. STOP ")

while True:
    os.system("clear")
    tm.sleep(1)
    key = int(input("enter your choice : "))
    if key == 1:
        a, b = int(input("enter 1st number : ")), int(input("enter 2nd number : "))
        print("Sum  of {} and {} is {} ".format(a,b,add(a,b)))

    elif key == 2:
        a, b = int(input("enter 1st number : ")), int(input("enter 2nd number : "))
        print("Sub : {} - {} is {} ".format(a, b, sub(a, b)))

    elif key == 3:
        a, b = int(input("enter 1st number : ")), int(input("enter 2nd number : "))
        print("Mul  of {} and {} is {} ".format(a, b, mul(a, b)))

    elif key == 4:
        a, b = int(input("enter 1st number : ")), int(input("enter 2nd number : "))
        print("Div  of {} / {} is {} ".format(a, b, div(a, b)))

    elif key == 5:
        a = int(input("enter a number : "))
        print("Factorial  of {}  is {} ".format(a, fact(a)))

    elif key == 6:
        a = int(input("enter a number : "))
        print("Cube root  of {}  is {} ".format(a, cube_root(a)))

    elif key == 7:
        a = int(input("enter a number : "))
        print("Sqar root  of {}  is {} ".format(a, sq_root(a)))

    elif key == 8:
        a, b = int(input("enter nth value : ")), int(input("enter the number : "))
        print("{} root  of {} is {} ".format(a, b, nth_root(a, b)))

    elif key == 9:
        a = int(input("enter a number : "))
        print("Sqar  of {}  is {} ".format(a, sqr(a)))

    elif key == 10:
        a = int(input("enter a number : "))
        print("Cube  of {}  is {} ".format(a, cube(a)))

    elif key == 11:
        a, b = int(input("enter nth value : ")), int(input("enter the number : "))
        print("{} sq_root  of {} is {} ".format(a, b, nth_sq(a, b)))

    elif key == 12 :
        break
    else:
        print(" Invalid choice ")

print("BYE BYE !!")

