
pos = -1


def search(lst, num):

    k = 0
    for i in lst:
        k += 1
        if i == num:
            globals()['pos'] = k
            return True
    else:
        return False


lst = [int(e) for e in input("enter your list by space separeted number: ").split()]

num = int(input("Enter the number to searched: "))

if search(lst, num):
    print("Found at ", pos)

else:
    print("Not Found ")