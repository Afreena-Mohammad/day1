#create an array and find sum of  array elements using functions
numbers_list=[1,5,7,5,1,4,3,7,8]
def get_total(numbers_list):
    total=0
    for num in numbers_list:
        total+=num
    return total

print(get_total(numbers_list))