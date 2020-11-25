

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


lst = [int(e) for e in input("Enter your sorted list by space separated numbers :  ").split()]

num = int(input("Enter the number to be searched :  "))

if search(lst, num):
    print("Found at ", pos + 1)
else:
    print("Not Found ")

