
# operator overloading


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        su = Student(m1, m2)
        return su

    def __sub__(self, other):
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        su = Student(m1, m2)
        return su

    def __gt__(self, other):
        m1 = self.m1 + self.m2
        m2 = other.m1 + other.m2
        if m1 > m2:
            return True
        else:
            return False

    def __str__(self):
        return " {} {} ".format(self.m1, self.m2)

    def __mul__(self, other):
        m1 = self.m1 * other.m1
        m2 = self.m2 * other.m2
        su = Student(m1, m2)
        return su


s1 = Student(int(input(" Enter one number : ")), int(input(" Enter other : ")))
s2 = Student(int(input(" Enter one number : ")), int(input(" Enter other : ")))
print("s1 is : ", s1)
print("s2 is : ", s2)
s3 = s1 + s2
print("Add is : ", s3)

s4 = s1 - s2
print("Sub is : ", s4)

s5 = s1 * s2
print("mul is : ", s5)

if s1 > s2:
    print("s1 Wins")
else:
    print("s2 Wins")
