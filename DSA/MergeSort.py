def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergeSort(arr):
    step = 1
    length = len(arr)
    
    while step < length:
        for i in range(0, length, 2 * step):
            left = arr[i:i + step]
            right = arr[i + step:i + 2 * step]
            
            merged = merge(left, right)
            for j, val, in enumerate(merged):
                arr[i+j]=val
        step *= 2
        
    return arr
unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array: ", sortedArr)


# -------------------------------------------------------------------------
def prefix_averagel(s):
    n = len(s)
    A = [0]*n
    for j in range(n):
        total = 0 
        for i in range(j+1):
           total += s[i]
        A[j] = total / (j + 1)
    return A
           
        