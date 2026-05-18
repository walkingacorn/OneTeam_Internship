# my_set={1,2,3,3,4}
# print(my_set)

#creating a set
# empty_set=set() #{} creates a dictionary
# set_with_elements={'apple','banana','cherry'}

#using set with iterables
# set_with_iterable=set([1,2,3,3,4])
# print(set_with_iterable)

#Basic set operations
# fruits={'apple','banana'}
# print(fruits)
# fruits.add('cherry')
# print(fruits)

# fruits.remove('banana') #throws error if not found
# print(fruits)
# fruits.discard('cherry') #does not throw error if not found
# print(fruits)
# fruits.clear()
# print(fruits)

#Mathematical set operations
# set1={1,2,3}
# set2={3,4,5}

# print(set1 | set2) #union of set1 and set2
# print(set1 & set2) #intersection
# print(set1 - set2) #difference
# print(set1 ^ set2) #symmetric difference


#common use cases of sets
#removing duplicates from a list
# names=['Alice','Anjali','Meghna','Anjali']
# set_names=set(names)
# print(list(set_names))

#membership testing
# print('Anjali' in set_names)

#set comparison
setA={1,2}
setB={1,2,3,4}

print(setA.issubset(setB))
print(setB.issubset(setA))
print(setB.issuperset(setA))