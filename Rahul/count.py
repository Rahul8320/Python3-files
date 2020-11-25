

def count(lst):
    ev = 0
    od = 0

    for e in lst:

        if e % 2 == 0:
            ev += 1
        else:
            od += 1

    return ev, od


print("Enter your list with space separated ")

lst = [int(e) for e in input().split()]

print("Your list is : {}".format(lst))

print("Your list have {} elements ".format(len(lst)))

even, odd = count(lst)

print("In Your list Even number is : {} and odd number is : {}".format(even, odd))
