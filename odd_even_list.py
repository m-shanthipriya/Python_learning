number_list = [1,2,3,4,5,6,7,99]
even = []
odd = []
for number in number_list:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print even
print odd

