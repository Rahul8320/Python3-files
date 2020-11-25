
import random as rn

pos = -1


def search(lst, num):
    l = 0
    u = len(lst) - 1
    while l <= u:
        mid = (l + u) // 2
        if lst[mid] == num:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < num:
                l = mid + 1
            else:
                u = mid - 1
    return False


lst = []
for i in range(100000):
    key = rn.randint(0, 100)
    lst.append(key)

lst.sort()
# print("Your list is : ", lst)

while True:

    num = int(input("Enter the number to be searched :  "))

    if search(lst, num):
        print("Found at ", pos + 1)
    else:
        print("Not Found ")

