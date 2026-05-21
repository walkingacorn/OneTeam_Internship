# class Animal:
#     def __init__(self,name):
#         self.name=name
        
#     def speak(self):
#         print(f"{self.name} makes a sound")
        
# class Dog(Animal):  #inheriting from animal
#     def speak(self):
#         print(f"{self.name} says Woof!")
        
# my_dog = Dog("Buddy")
# # my_animal=Animal("Animal")
# my_dog.speak()
# # my_animal.speak()


#Basic Syntax of inheritance
# class Parent:
#     def display(self):
#         print("This is the parent class.")
# class Child(Parent):
#     pass

# c=Child()
# c.display()


#using super in inheritance

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
class Employee(Person):
    def __init__(self,name,age,emp_id):
        super().__init__(name,age)
        self.emp_id=emp_id
        
e=Employee("John",30,'E123')
print(e.name,e.age,e.emp_id)