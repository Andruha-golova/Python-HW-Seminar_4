import random

n = int(input('Enter the number of elements of the first occurrence: '))
m = int(input('Enter the number of elements of the second occurence: '))


col_1 = {random.randint(1, 15) for i in range(n)}
print(col_1)
col_2 = {random.randint(1, 15) for i in range(m)}
print(col_2)
col_3 = print(sorted(col_1.intersection(col_2)))