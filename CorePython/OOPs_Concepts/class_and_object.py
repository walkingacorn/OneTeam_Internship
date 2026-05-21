class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
        
    def display_details(self):
        print(f"Car: {self.brand} {self.model}, Year:{self.year}")
        
#Creating objects from the class
my_car=Car("Toyota","Corolla",2020)
your_car=Car("Honda","Civic",2019)

#Accessing methods
my_car.display_details()
your_car.display_details()