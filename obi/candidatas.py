inp1 = [int(x) for x in input().split()]

seq = [int(x) for x in input().split()]


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def candidata(arr = []):
    count = 0
    lengh = len(arr)
    for i in range(0,lengh+1):
        for j in range(i,lengh):
            
            subseq = arr[i:j+1]
            compare = subseq[0]
            for num in subseq:
                compare = gcd(compare, num)
            if compare>1:
                count+=1
                
    return count

res = []

for i in range(inp1[1]):
    op = [int(x) for x in input().split()]
    if op[0] == 1:
        seq[op[1]-1] = op[2]
    
    if op[0] == 2:
        res.append(candidata(seq[op[1]-1:op[2]]))

for i in res:
    print(i)
