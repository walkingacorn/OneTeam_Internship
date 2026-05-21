class Person:
    def describe(self):
        print("I am a person.")
        
class Student(Person):
    def describe(self):
        print("I am a student.")
        
class Teacher(Person):
    def describe(self):
        print("I am a teacher.")
        
#Polymorphism in action
people=[Person(),Student(),Teacher()]
for person in people:
    person.describe()