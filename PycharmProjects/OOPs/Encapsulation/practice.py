# Example-1
'''
# Creating a Base
class Base:
    def __init__(self):

        # protected member
        self._a = 2

# Creating a derived class
class Derived(Base):
    def __inti__(self):

        # calling constructor of base class
        Base.__init__(self)
        print("Calling protected member of base class: ", self._a)

        # Modify the protected variable:
    def display(self):
        self._a = 3
        print("Calling modified protected base class: ", self._a)


obj1 = Derived()
obj1.display()
obj2 = Base()
print(obj1._a)

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)'''

