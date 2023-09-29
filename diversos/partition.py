#https://www.youtube.com/watch?v=ngCos392W4w problema 3
def partition(n, m):
    if n == 0:
        return 1
    if m == 0:
        return 0
    
    ene = n
    while True:
        ene -= m
        if ene > m or ene == m:
            print(f'ene > maior que m, {ene}')
        else:
            print(f'ene menor que m , {ene}')
            break
    
    return partition(n, m-1) + partition(m-n, m)



    


#VSF Q BAGULHO DIFICIL VO FAZE DPSKKKKKKKKKK


print(partition(5,3))