#positional argument

# def greet(name):
#     print("Hello",name)
# greet("Anjali")


#default argument

# def greet(name="Friend"):
#     print("Hello",name)
# greet("Anu")


#keyword argument

# def introduce(name,age):
#     print(f"Hello I am {name}. I am {age} years old.")
# introduce(age=23,name="Anjali")

#create a function calculate_total(price,tax=5) that calculates the total cost after adding tax

# def calculate_total(price,tax=5):
#     total_cost=price+ (price*tax/100)
#     return total_cost

# price=int(input("Enter the price of the item:"))
# print(f"The total price is {calculate_total(price)}")

#suqare of a num
# def square(num):
#     return num*num
# number=int(input("Enter a number to find the square of:"))
# print(square(number))

#calculations using mutliple return arguments
# def simultaneous(a,b):
#     return f"Sum:{a+b} and Diff:{a-b}"
# a=int(input("Enter first number:"))
# b=int(input("Enter the second number:"))
# print(simultaneous(a,b))

#get grade
def get_grade(marks):
    if marks>=95 and marks<=100:
        print('Congratulations, you have high distinction. Your grade is S')
    elif marks>=85 and marks<95:
        print('Your grade is A')
    elif marks>=75 and marks<85:
        print('Your grade is B')
    elif marks>=65 and marks<75:
        print('Your grade is C')
    elif marks>=50 and marks<65:
        print('Your grade is D')
    elif marks>=0 and marks<50:
        print('Your failed. Your grade is F')
    else:
        print("Invalid marks. Enter a number between 0 and 100")
        
marks=int(input("Enter your marks:"))
get_grade(marks)
        
    