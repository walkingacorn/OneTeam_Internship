#nested while loop 
# i=1
# while i<=3:
#     j=1
#     while j<=2:
#         print("Hello")
#         j+=1
#     print('Hai')
#     i=i+1



#nested for loop
# for i in range(3):
#     for j in range(2):
#         print('Hello')
#     print('Hai')

# pattern: * * * * *
# for i in range(5):
#     print('*', end=" ")
    
#row n in each row
# for i in range(1,6):
#     print(f"Row {i}")

'''Pattern 
* * * *
* * * *
* * * *
* * * *
'''
# for i in range(4):
#     for j in range(4):
#         print('*',end=" ")
#     print()

'''
Right Angle Triangle pattern
*
* *
* * *
* * * *
'''

# for i in range(1,5):
#     for j in range(i):
#         print("*",end=" ")
#     print()

'''
Inverted Triangular Pattern
* * * *
* * *
* *
*
'''

# for i in range(4,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

'''
Pyramid Printing
    *
   * *
  * * *
 * * * *
* * * * *
'''

for i in range(4,-1,-1):
    for j in range(i):
        print(" ",end="")
    print()
        
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
