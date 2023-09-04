# comiteiro
def bestSum(n,arr = []):
    if n == 0:
        return []
    if n<0: 
        return None
    
    theBest = None

    for i in arr:
        sub = n-i
        res = bestSum(sub, arr)
        if res is not None:
            res.append(i)
            print(res)
            if theBest is None or theBest < res:
                theBest = res

    return theBest


print(bestSum(8,[1,4,5]))