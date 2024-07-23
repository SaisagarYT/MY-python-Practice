class Student:
    def __init__(self,name,rollno,age):
        self.name = name
        self._roolno = rollno
        self.__age = age

    def get_age(self):
        return self.__age
    def set_age(self,num):
        self.__age = num
    # def __display(self):
    #     print(f"Hi myself {self.name} with rollno {self._roolno} from student class of age {self.__age}")
    # def ageDisplay(self):
    #     print(self.__age)
    # def displayPrivateData(self):
    #     self.__display()

# class Branch(Student):
#     def show(self):
#         print(f"My rollno is {self._roolno}")
#
# s1 = Student("rahul",23,12)
# s1.ageDisplay()
#
# # Using name Mangling
# s1._Student__display()
# s1._Student__age = 23
# s1._Student__display()
# print(s1._Student__age)

s1 = Student("sai",12,20)
s1.set_age(24)
print(s1.get_age())