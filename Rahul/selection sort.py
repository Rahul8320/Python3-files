

def swap(a, b):
    a, b = b, a
    return a, b


def sort(lst):
    for i in range(len(lst)-1):
        minpos = i
        for j in range(i, len(lst)):
            if lst[j] < lst[minpos]:
                minpos = j

        lst[i], lst[minpos] = swap(lst[i], lst[minpos])


lst = [int(e) for e in input("Enter the list : ").split()]

sort(lst)

print("Your sorted list is ", lst)

