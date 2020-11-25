
import random as rn

pos = -1


def search(lst, num):
    k = 0
    for i in lst:
        if i == num:
            k += 1

    globals()['pos'] = k
    if k != 0:
        return True
    else:
        return False


lst = []
for e in range(100000):
    key = rn.randint(0, 100)
    lst.append(key)

# print("Your list is : ", lst)
while True:
    num = int(input("Enter the number to searched: "))

    if search(lst, num):
        print("Found as {} times ".format(pos))

    else:
        print("Not Found")

