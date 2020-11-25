

def swap(a, b):
    a, b = b, a
    return a, b


def sort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = swap(lst[j], lst[j+1])


lst = [int(e) for e in input("Enter your list by space separated numbers : ").split()]

sort(lst)

print("Sorted ist is :  ", lst)
