def inverted_num():
    for i in range(5,1,-1):
        for j in range(1,i):
            print(j,end="")
        print()

def pyramid():
 for i in range(1,8,2):
    print(" "*((8-i)//2)+"*"*i)
    
def sum_of_first_n(n):
    if n==0:
        return 0
    else:
        return n+sum_of_first_n(n-1)
    
    
print("LMS TASK - WEEK 3")

while True:
   
    print("1.Print Pyramid Star Pattern")
    print("2.Print Inverted Number Pattern")
    print("3.Calculate Sum of First N natural numbers")
    print("4.Calculate power of a number using lambda function")
    
    choice=int(input("Choose an option:(1-5)"))
    
    if choice==5:
        print("Thank you.")
        break
    
    if choice in [1,2,3,4]:
        if choice == 1:
            pyramid()
            
        elif choice == 2:
            inverted_num()
            
        elif choice == 3:
            num=int(input("Enter the value for n:"))
            print(sum_of_first_n(num))
            
        elif choice == 4:
            num=int(input("Enter number:"))
            power = int(input("Enter power:"))
            power_of_num=lambda num,power:num**power
            print(power_of_num(num,power))
            
        
    else:
        print("Invalid Choice!")
            
    
    

