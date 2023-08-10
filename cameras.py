

inp1 = [int(x) for x in input().split()]

def matrix(y,x,c):
    mtx = [True] * y
    mtx = [mtx] * x
    for cam in c:
        if cam[2] == 'N':
            mtx[cam]
            for i in range(0,cam[1]):
                mtx[i][cam[0]-1] = False
        if cam[2] == 'S':
            for i in range(cam[1],y):
                mtx[i][cam[0]-1] = False
        if cam[2] == 'O':
            for i in range(0,cam[0]):
                mtx[cam[1]-1][i] = False
        if cam[2] == 'L':
            for i in range(cam[0],x):
                mtx[cam[1]-1][i] = False

    return mtx



def valid(mtx, moves):
    i,j = 0,0
    l = len(mtx[0])-1
    h = len(mtx)-1
    for move in moves:
        match move:
            case 'L':
                j -= 1
            case 'R':
                j += 1
            case 'U':
                i -= 1
            case 'D':
                i += 1
        
        if (i < 0 or j < 0) or (i > h or j > l):
            return False
        if not mtx[i][j]:
            return False
    return True


def findEnd(mtx, moves):
    i,j = 0,0
    l = len(mtx[0])-1
    h = len(mtx)-1
    for move in moves:
        match move:
            case 'L':
                j -= 1
            case 'R':
                j += 1
            case 'U':
                i -= 1
            case 'D':
                i += 1
        
    if j == l and i == h:
        return True
    
def dfs(mtx):
    #puta que pariu que bagulho dificil eu vo dormir agr pfv qnd eu acordar que recursao esteja na minha cabeca amem