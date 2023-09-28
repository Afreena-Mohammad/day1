#linear search using functions
def lin_search(arr,se):
    for i in range(len(arr)):
        if arr[i]==se:
            return i
    return -3
my_array=list(map(int,input().split(" ")))
se_element=int(input())
result=lin_search(my_array,se_element)
if result!=-3:
    print(f"element {se_element} found at index {result}")
else:
    print(f"element {se_element} not found at  any index")


