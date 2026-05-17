#Write a recursive function to calculate the sum of numbers from 1 to n

# def sum_add(n):
#     if n==1:
#         return 1
#     else:
#         return n + sum_add(n-1)
    
# print(sum_add(5))



#Fibonacci

# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
    
# print(fibonacci(6))

# def fib(n):
#     a,b=0,1
#     i=0
    
#     while(i<n):
#         print(a,end=" ")
#         a,b=b,a+b
#         i+=1
        
# fib(6)


#sum of a list of numbers
# def sum_list(lst):
#     if len(lst)==0:
#         return 0
#     else:
#         return lst[0]+sum(lst[1:])
    
# print(sum_list([1,2,3,4]))

#Write a recursive function to reverse a string

# def reverse_string(s):
#     if len(s)==0:
#         return s
#     else:
#         return reverse_string(s[1:])+s[0]

# print(reverse_string("hello"))


#recusively sum the elements of a list

# list1=[1,2,3,4,5]

# def sum_list(list1):
#     if len(list1)==0:
#         return 0
#     else:
#         return list1[0] + sum_list(list1[1:])
    
# print(sum_list(list1))


#reverse a string

# string1="hello"

# def rev_string(string1):
#     if len(string1)==0:
#         return ''
#     else:
#         return rev_string(string1[1:])+string1[0]
    
# print(rev_string(string1))