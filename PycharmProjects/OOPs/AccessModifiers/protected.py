class Student:
    def __init__(self,name,rollno):
        self.name = name
        self._roolno = rollno
    def display(self):
        print(f"Hi myself {self.name} with rollno {self._roolno} from student class")

class Branch(Student):
    pass

s1 = Student("sagar",20)
s1.display()
print(s1._roolno)
print(s1.name)

def ShowData():
    s1 = Branch("sagar",10)
    s1.display()
    print(s1._roolno)

ShowData()

