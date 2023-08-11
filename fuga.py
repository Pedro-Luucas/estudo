def matrix(l,c):
    mtx = [0] * c
    mtx = [mtx] * l
    cont = 1
    cont1 = 1
    for i in mtx:
        if cont % 2 == 0:
            for j in i:
                if cont1 % 2 == 0:
                    mtx[cont-1][cont1-1] = 1


    return mtx



mtx = [int(x) for x in input().split()]
start = [int(x) for x in input().split()]
end = [int(x) for x in input().split()]

maior = 0
atual = 0
grid = matrix(mtx[0],mtx[1])
cs = start[0]-1
ls = start[1]-1
cend = end[0]-1
lend = end[1]-1
lsoma = [1,-1,0,0]
csoma = [0,0,-1,1]

def dfs(l,c):
    grid[l][c] = 1
    atual += 1

    if l == lend and c == cend:
        maior = max(maior, atual)
    for i in range(4):
        ll = l + lsoma[i]
        cc = c + csoma[i]
        if ll>=0 and cc>=0 and ll<=(len(grid)-1) and cc<=(len(grid[0])-1) and grid[ll][cc] == 0:
            dfs(ll,cc)

    grid[l][c] = 0
    atual -= 1
    

print(maior)

