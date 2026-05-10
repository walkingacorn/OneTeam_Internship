#1.Print numbers from 10 to 1(while loop)
# i=10
# while i>0:
#     print(i,end=" ")
#     i-=1
    
    
#2. Print even numbers between 1 and 20
# i=1
# while i<=20:
#     if i%2==0:
#         print(i,end=" ")
#     i+=1

        
#3. Multiplication table
# num=int(input("Enter a number you want multiplication table of:"))
# for i in range (1,11):
#     print(f"{num} X {i} = {num*i}")
    
    
#4.Sum of first n natural numbers using for loop
# limit=int(input("Enter a limit:"))
# sum=0
# for i in range(1,limit+1):
#     sum+=i
# print(f"Sum of first {limit} numbers is {sum}")


#5. Reverse a number (while loop)
# num=int(input("Enter a number to be reversed:"))
# rev=0
# rem=0
# while num>0:
#     rem=num%10
#     rev=rem+rev*10
#     num=num//10
# print(rev)


#6. Largest number in list
# num_list=[1,2,3,4,5,6,9]
# temp=num_list[0]
# for num in num_list:
#     if num>temp:
#         temp=num
# print(temp)       
    
    
#7. Prime number check
num=int(input("Enter a number:"))
if num<=1:
    print("It is not prime")
else:
    i=2
    while i<=num//2:
        if num%i==0:
            print("It is not prime")
            break
        i+=1
    else:
        print("It is prime")
    

#8. Count digits
   
#9. Fibonacci series
#10. Factorial