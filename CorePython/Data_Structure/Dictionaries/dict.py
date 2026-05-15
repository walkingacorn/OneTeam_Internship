# my_dict={"name":"Alice","age":25,"city":"New York"}
# print(my_dict)
# print(type(my_dict))

#Creating Dictionaries

# empty_dict={}
# empty_dict = dict()



# my_dict.update({"place":"kannur"}) #to modify a dictionary
# print(my_dict)


#Nested dictionaries
# student={"student1":{"name":"Anjali","age":"23"},"student2":{"name":"Meghna","age":22}}
# print(student.get('student1').get('name'))
# print(student['student1']['name'])


# #Accessing values
#student = {"name":"Anjali","age":"23","test":"test_text","marks":80}
# print(student1['name'])

#Removing elements 

# student.pop("age")
# print(student)

# del student["marks"]
# print(student)

# student.popitem()
# print(student)

# student.clear()
# print(student)


#Common methods
student={"name":"John","marks":85,"age":"20"}
# print(student.keys())  #dict_keys(['name', 'marks', 'age'])
# print(student.values()) #dict_values(['John', 85, '20'])
# print(student.items())  #dict_items([('name', 'John'), ('marks', 85), ('age', '20')])


#Using get method
# print(student.get("marks")) #85
# print(student.get('grade','Not available'))


#Updating a dictionary
# student.update({'marks':90,'grade':'A'})
# print(student)


#Membership testing
print('name' in student) #True
print('grade' in student) #False