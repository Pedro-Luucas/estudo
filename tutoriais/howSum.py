def howSum(n, arr):
    if n == 0:
        return 1
    if n < 0:
        return 0
    
    res = 0
    for i in arr:
        sub = n-i
        res += howSum(sub, arr)

    
    return res


print(howSum(4,[1,2,3]))