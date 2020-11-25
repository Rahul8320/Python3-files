
def count(lst):

    temp = 0
    for e in lst:

        if len(e) > 5:

            temp += 1

    return temp


print("Enter names of employees with space separated : ")

lst = [e for e in input().split()]

print("Your employees list is : \n\n {} \n\n and list have {} numbers of employees".format(lst,len(lst)))

tem = count(lst)

print("\n {} number of employess name have >5 letters".format(tem))
