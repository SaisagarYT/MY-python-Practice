# ADDING TWO OBJECTS USING __add__()...
'''class complexNumbers:
    def __init__(self, r, i):
        self.real = r
        self.image = i
    def __add__(self,other):
        return f"{self.real + other.real} + {self.image + other.image}i"

c1 = complexNumbers(1, 2)
c2 = complexNumbers(3, 6)

# print(c1+c2) //it is not possible...
# After declaring the __add__function

print(c1+c2)'''

# WHO PAYS THE BILL ?
'''class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __gt__(self,other):
        if self.age < other.age:
            return True
        else:
            return False
p1 = person("sai",19)
p3 = person("gowtham", 23)
if(p1 < p3):
    print(f"{p1.name} will pay teh bill")
else:
    print(f"{p3.name} will pay the bill")'''


# Example - 1
'''class A:
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        return self.a + other.a

a = A(10)
b = A(20)
# print(a+b)
print(A.__add__(a,b))

a  = A("sai")
b = A("sagar")
# print(a+b)
print(A.__add__(a,b))'''





