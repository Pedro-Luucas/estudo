# https://www.youtube.com/watch?v=ngCos392W4w 2° problema
def gridTraveler(h,l):
    if h==2 and l == 2:
        return 2
    menor = h if l>h else l
    maior = l if l>h else h
    if menor == 2:
        return maior
    
    return gridTraveler()