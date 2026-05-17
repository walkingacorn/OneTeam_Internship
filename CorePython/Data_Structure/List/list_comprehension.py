#creating lists with simple expressions
# numbers=[x for x in range(10)]
# print(numbers)

# even_numbers=[x for x in range(10)if x%2==0]
# print(even_numbers)

# matrix=[[x for x in range(3)] for y in range(3)]
# print(matrix)

# #Flattening
# nested=[[1,2],[3,4],[5,6]]
# flat=[num for sublist in nested for num in sublist]
# print(flat)


# #Characters
# vowels=[char for char in "hello world" if char in "aeiou"]
# print(vowels)


#combining multiple conditions
# special_numbers=[x for x in range(101) if x%2==0 and x%5==0]
# print(special_numbers)


#Using function within comprehension
# def squares(x):
#     return x*x

# squares=[squares(x) for x in range(1,6)]
# print(squares)

matrix=[[x for x in range(3)] for y in range(3)]
print(matrix)

squares=[x**2 for x in range(5)]
print(squares)

test1='I love python, python is amazing'
print(test1.find('python'))
print(test1.rfind('python'))