# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# for row in matrix:
#     for number in row:
#         print(number,end=" ")
#     print()
    
'''
print pattern
*
**
***
****
'''

for i in range(1,5):
    for j in range(i):
        print('*',end='')
    print()

#multiplication table from 1 to 5

for i in range(1,6):
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")
        
    print()