list_of_number = [11,1,2,3,4,5,6,7,8,9,10]
#list_of_number = ['a','b','c']


def largest_num_from_the_list(list_of_number):
    max_number = list_of_number[0]  #max_number = []
    for item_from_a_list in list_of_number:
        if item_from_a_list > max_number:
            max_number = item_from_a_list   #Setting the max number in the loop flow
    return max_number   #Not printing inside the function, so using retrun function


print largest_num_from_the_list(list_of_number)

