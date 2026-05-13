# lst = [1,2,3,4,2,'red','blue','green']
# print(lst)
# print(type(lst))
# print(lst[5])
# print(lst[-2])
# print(lst[1:5])
# print(lst[3:])
# print(lst[:6])
# print(lst[-6:-2])

# print(len(lst))

#concatenation, repetition, membership, length

#picnic_items=['water','sandwich','umbrella','bag','clothes']

# people=["Sam","Mary","Michael"]

# picnic = picnic_items + people

# print(picnic)

# people1 = people*3
# print(people1)

# print("juice" in picnic_items)
# print("juice" not in picnic_items)

#List Methods - Adding Elements

# picnic_items.append('fruit')
# # print(picnic_items)
# picnic_items.insert(2,'soda')
# # print(picnic_items)
# picnic_items.extend(['cake','icecream'])
# print(picnic_items)

#List Methods - Removing Elements

# picnic_items.remove('sandwich')
# print(picnic_items)
# picnic_items.pop(2)
# print(picnic_items)
# picnic_items.clear()
# print(picnic_items)


#Sorting
# fruits=["banana","apple","cherry"]
# fruits.sort()
# print(fruits)

# numbers=[3,1,4,1,5]
# print(sorted(numbers)) #returns a new sorted list

# print(fruits.index("cherry"))
# print(numbers.count(1))
# fruits.reverse()
# print(fruits)


#Nested List
# picnic_bags=[['sandwich','juice'],['chips','soda'],['cookies','milk']]

# print(picnic_bags[1][1])
# print(picnic_bags[1][3]) #Index Error List out of range


# numbers=[[3,2,1],[6,5,4],[8,9,7]]
# numbers.reverse()
# print(numbers)
# largest=max(numbers)
# print(largest)
# smallest=min(numbers)
# smallest1=min(numbers[0])
# print(smallest)
# print(smallest1)
# numbers.sort()
# print(numbers)