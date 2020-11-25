
from functools import reduce

lst = [2, 5, 9, 4, 6, 8, 3, 1, 15, 16, 14, 18, 19, 14]


even = list(filter(lambda n: n % 2 == 0, lst))

print('even list is: ',even)

double = list(map(lambda n: n*2,even))

print("double list is : ",double)

sum = reduce(lambda a, b: a+b, double)

print(sum)
