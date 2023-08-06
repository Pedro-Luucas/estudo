import math

#funcao q retorna multiplicacoes possiveis
def mult_poss(x):
    poss = []
    lim = int(math.sqrt(x)) + 1
    for i in range(1, lim):
        if x % i == 0:
            j = x // i
            poss.append((i, j))
    return poss

#funcao q adiciona 2 a todos os elementos da lista
add = lambda lista: [(x[0] + 2, x[1]+2) for x in lista]


def quad(a,b):
    bPoss = mult_poss(b)
    bPoss = add(bPoss)
    aPoss = mult_poss(a+b)
    for i in aPoss:
        for j in bPoss:
            if i == j:
                return j
    return (-1,-1)

a = int(input())
b = int(input())
l = quad(a,b)
for i in l:
    print(i, end=' ')
    