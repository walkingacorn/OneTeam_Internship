#----------------------------STRING TASK--------------------------------------
#1.extract the first and last character of a string
# name="Anjali"
# print([name[0],name[-1]])

#2.reverse a string
# string1='Misrepresented'
# print(string1[::-1])

#3.count occurences of a specific character
# string1='Misrepresented'
# print(string1.count('e'))

#4.replace spaces with underscores
# string2="Python is a programming language."
# string3=string2.replace(" ","_")
# print(string3)

#5.check if a string is a palindrome
# string4=input("Enter a string:")
# if (string4.lower()==string4[::-1].lower()):
#     print("it is a palindrome")
# else:
#     print("it is a not a palindrome")
    





#----------------------------TUPLE TASK--------------------------------------
#create a tuple with the names of the days of the week, access specific elements, slice the tuple and find the index of 'wednesday'

# days_of_week=('sunday','monday','tuesday','wednesday','thursday','friday','saturday')
# print(days_of_week)
# print(days_of_week[4])
# print(days_of_week[-2])
# print(days_of_week[3:6])
# print(days_of_week.index('wednesday'))




#----------------------------SET TASK--------------------------------------
#create a set of uniques student names from a list.
student_name_list=['Anjali','Irene','Meghna','Dilsha','Ashigha','Arsha']
student_name_set=set(student_name_list)
print(student_name_set)

#perform union intersection and difference operation on two sets of numbers
num1={1,2,3,4}
num2={3,4,5,6}
print(num1 | num2)
print(num1 & num2)
print(num1 - num2)
print(num1 ^ num2)

#check if one set is a subset of other
setA={1,2}
setB={1,2,3,4}
print(setA.issubset(setB))
print(setB.issubset(setA))