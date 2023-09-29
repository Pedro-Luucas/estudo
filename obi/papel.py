n = int(input())
papel = [int(x) for x in input().split()]
sortedPapel = sorted(papel)


indiValue = []

def corte(papel,pivo):
    pedacos = 1
    anterior = 0
    for i in papel:
        if i > pivo and anterior < pivo:
            pedacos += 1
        anterior = i
    return pedacos

anterior = 0
for i in sortedPapel:
    pivo = i-1
    if pivo in indiValue:
        continue
    ped = corte(papel, pivo)
    if anterior > ped:
        break
    indiValue.append(pivo)
    anterior = ped

#dando errado n sei pq
print(anterior)