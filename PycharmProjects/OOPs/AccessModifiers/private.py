class Student:
    def __init__(self,name,rollno,age):
        self.name = name
        self._roolno = rollno
        self.__age = age
    def display(self):
        print(f"Hi myself {self.name} with rollno {self._roolno} from student class of age {self.__age}")
    def ageDisplay(self):
        print(self.__age)
class Branch(Student):
    pass

s1 = Student("sagar",20,12)
s1.display()
print(s1._roolno)
print(s1.name)
s1.ageDisplay()
def ShowData():
    s1 = Branch("sagar",10,12)
    s1.display()
    print(s1._roolno)
ShowData()

