full_list = [1, 2, 3, 1, 2,2,2,2,2,22,2, 5, 6, 7, 8]
# full_list = ['a','b','c', 'c', 'c']
unique_list = []

for value in full_list:
    if value not in unique_list:
        unique_list.append(value)
        unique_list.sort()
print unique_list[-2]


