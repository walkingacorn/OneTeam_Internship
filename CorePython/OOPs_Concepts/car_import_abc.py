from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
class Car(Vehicle):
        def start(self):
            print("car is starting..")
            
        def stop(self):
            print("car is stopping..")
            
class Bike(Vehicle):
    def start(self):
            print("bike is starting..")
            
    def stop(self):
            print("bike is stopping..")
            
car=Car()
bike=Bike()

car.start()
car.stop()
bike.start()
bike.stop()
            
            