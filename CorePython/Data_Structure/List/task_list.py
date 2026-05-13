#1.Find the sum of all elements in a list
# numbers=[1,2,3,4,5]
# print(sum(numbers))



#2. Find the average of list elements
# average=sum(numbers)/len(numbers)
# print(average)



#3. Remove duplicate lements from a list
# num=[1,2,1,3,4,5,5,2,6,7,8]
# num2=set(num)
# num3=list(num2)
# print(num3)
# count vechum cheyyam


#4.Merge two lists into one
# list1 = [1,2,3,4,5]
# list2 =['apple','banana']
# list3 =list1+list2
# print(list3)



#5. Find the second largest element in a list
# num=[1,2,3,3,4,6,3,1,7,5,4,3,1,6,8,5,4]
# num1=sorted(num)
# print(num1[-2])

#6. Find even and odd numbers from a list
# num=[1,2,3,3,4,6,3,1,7,5,4,3,1,6,8,5,4]
# even=[]
# for item in num:
#     if item%2==0:
#         even.append(item)
    
# print(list(set(even)))



#7. Create a new list containing squares of elements
# num=[1,2,3,3,4,6,3,1,7,5,4,3,1,6,8,5,4]
# squares=[]
# for item in num:
#     squares.append(item**2)
    
# print(squares)



#8. Find common elements between two lists
# list1=[1,2,3,4,5,6]
# list2=[4,5,6,7,8,9]
# list3=[]

# for item in list1:
#     if item in list2:
#         list3.append(item)
        
# print(list3)



#9. Find the index position of an element
# list1=[1,2,3,4,5,6]
# print(list1.index(4))



#10. rotate a list to left by one position (output[2,3,4,5,1])
# num=[1,2,3,4,5]
# print(num[1:]+num[:1])