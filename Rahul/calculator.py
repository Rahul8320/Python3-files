

def add(a, b):
    c = a + b
    return c


def sub(a, b):
    c = a - b
    return c


def mul(a, b):
    c = a*b
    return c


def div(a, b):
    c = a/b
    return c


def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f


def cube_root(x):
    ans = 0
    for i in range(0, abs(x) + 1):
        if ans ** 3 >= abs(x):
            break
        else:
            ans += 1
    if ans ** 3 != abs(x):
        return "NULL"
    else:
        if x < 0:
            ans = - ans
        return ans


def sq_root(x):
    ans = 0
    for i in range(0, abs(x) + 1):
        if ans ** 2 >= abs(x):
            break
        else:
            ans += 1
    if ans ** 2 != abs(x):
        return "NULL"
    else:
        if x < 0:
            ans = str(ans)
            return ans+'i'
        return ans


def nth_root(nth, num):
    ans = 0
    for i in range(0, abs(num) + 1):
        if ans ** nth >= abs(num):
            break
        else:
            ans += 1
    if ans ** nth != abs(num):
        return "NULL"
    else:
        if num < 0 and nth % 2 != 0:
            ans = - ans
        return ans


def sqr(n):
    c = n*n
    return c


def cube(n):
    c = n*n*n
    return c


def nth_sq(nth, num):
    c = 1
    for i in range(nth):
        c = c * num
    return c

