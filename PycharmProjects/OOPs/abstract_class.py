from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,n):
        self.no_of_tyres = n
    @abstractmethod
    def start(self):
        pass
    def display(self):
        print("Hi i am from vehicle class")
