def matrix(l,c):
    mtx = [0] * c
    grid = []
    for i in range(l):
        grid.append(mtx[:])
    for i in range(l):
        for j in range(c):
            if i % 2 != 0 and j % 2 != 0:
                grid[i][j] = 1

    return grid


mtx = [int(x) for x in input().split()]
llen = mtx[0]-1
clen = mtx[1]-1
grid = matrix(mtx[0], mtx[1])

start = [int(x) for x in input().split()]
end = [int(x) for x in input().split()]

maior = 0
atual = 0
cs = start[0]-1
ls = start[1]-1
cend = end[0]-1
lend = end[1]-1
lsoma = [0,0,-1,1]
csoma = [1,-1,0,0]


def valid(l,c):
    global grid,llen,clen
    if l>=0 and c>=0 and l<=(llen) and c<=(clen):
        if grid[l][c] == 0:
            return True
    return False


def dfs(l,c):
    global grid
    global atual
    global lend
    global cend
    global maior
    global lsoma
    global csoma

    if valid(l,c):
        grid[l][c] = 1
    
    atual += 1

    if l == lend and c == cend:
        maior = max(maior, atual)
    for i in range(4):
        ll = l + lsoma[i]
        cc = c + csoma[i]
        if valid(ll,cc):
            dfs(ll,cc)

    grid[l][c] = 0
    atual -= 1


dfs(ls,cs)

print(maior)
