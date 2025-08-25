def binarySearch(arr, targetValu):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == targetValu:
            return mid
        
        if arr[mid] < targetValu:
            left = mid + 1
        else:
            right = mid - 1
    return -1

myArray = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
myTarget = 15
result = binarySearch(myArray, myTarget)

if result != -1:
    print("Value", myTarget, "found at index ", result)
else:
    print("target not found in the array.")
        
        