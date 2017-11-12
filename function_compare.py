name = raw_input('Enter name:')
animal = raw_input('Enter animal:')
def nameFunction(nam): # make him common
    name_length = 0
    for i in (nam): # make him common
        name_length=name_length+1
    # print(name_length)
    return name_length
nameFunction(name)
nameFunction(animal)
var = nameFunction(name)
var_01 = nameFunction(animal)
if var == var_01:
    print(str(name) + str(animal))
elif var > var_01:
     print (str(name))
elif var < var_01:
     print(str(animal))
else:
    print('Happy day')

# 1. get two inputs
# 2. get length
# 3. compare both
# 4. print which one is greater in length
