my_array = [64,34,25,12,22,11,90,5]

# version: 1
""" n = len(my_array)
for i in range(1,n):
    insert_index = i
    curreent_value = my_array.pop(i)
    for j in range(i-1,-1,-1):
        if my_array[j] > curreent_value:
            insert_index = j
    my_array.insert(insert_index,curreent_value)
print("sorted array:", my_array )    """ 

# version: 2
def InsertionSort(my_array):
    for num in range(1,len(my_array)):
        value = my_array[num]
        serial = num
        while serial > 0 and my_array[serial-1] > value:
            my_array[serial] = my_array[serial-1]
            serial = serial -1
        my_array[serial]=value
        print(my_array)
    return my_array

result = InsertionSort(my_array)
print(result)