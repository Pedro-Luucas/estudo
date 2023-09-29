#sum all elements array recursive
def sumAll(arr = []):
    if len(arr) == 1:
        return arr[0]
    
    a = arr[-1]
    arr.pop()
    return a + sumAll(arr)

print(sumAll([2,3,5]))