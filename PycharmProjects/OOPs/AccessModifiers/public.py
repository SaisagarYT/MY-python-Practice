class Student:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(f"Hi myself {self.name} from student class")
s1 = Student("sagar")
s1.display()
print(s1.name)