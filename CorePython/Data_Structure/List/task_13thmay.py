# #1.generate squares of numbers from 1 to 10 using list comprehension
# def squares(x):
#     return x*x

# squares=[squares(x) for x in range(1,11)]
# print(squares)


# #2.Extract all vowels from the string 'Python Programming is fun!'
# extract_vowels=[char for char in 'Python Programming is fun!'if char in 'aeiou']
# print(extract_vowels)



# #3.Filter out even numbers from a list of integers from 1 to 20
# filter_even=[x for x in range(1,21)if x%2==0]
# print(filter_even)

#negative number in list should become 0

def number(n):
    if(n<=0):
        return 0
    else:
        return n
        
list_numbers=[-3,-2,1,3,-6,4,2,-9,0,5,-8]
converted_list=[number(x) for x in list_numbers]
print(converted_list)

#alternate way: result = [x if x>0 else 0 for x in numbers]
#multiplication table

# def multiply(x):
    

# num=int(input("Enter a number")) 
multiplication_table=[5*x for x in range(1,11)]
print(multiplication_table)