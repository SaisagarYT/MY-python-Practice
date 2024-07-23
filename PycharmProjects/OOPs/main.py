from abstract_class import Vehicle
class Bike(Vehicle):
    def __init__(self,n,color):
        super().__init__(n)
        self.no_of_tyres = 2
        self.color = color
    def start(self):
        print("Start with kick")
class Scooty(Vehicle):
    def __init__(self,n):
        self.no_of_tyres = n
    def start(self):
        print("self start")
class car(Vehicle):
    def __init__(self,n,x):
        super().__init__(n)
        self.no_of_gears = 6
    def start(self):
        print("Start with key")

