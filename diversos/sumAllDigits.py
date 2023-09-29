#sum all digits of a number recursive
def sumAllDigits(num):
    strNum = list(str(num))
    if len(strNum) == 1:
        return int(strNum[0])
    
    a = int(strNum[-1])
    strNum.pop()
    remainNum = ''.join(strNum)
    return a + sumAllDigits(int(remainNum))

print(sumAllDigits(2341))