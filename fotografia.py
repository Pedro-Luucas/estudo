
hxvb = [int(x) for x in input().split()]
a = hxvb[0]
l = hxvb[1]
n = int(input())
molduras = []
for i in range(n):
    mol = [int(x) for x in input().split()]
    molduras.append(mol)

cont = 0
melhor = -1
menorDelta = 1000000
for mold in molduras:
    soma = 1
    cont += 1
    for j in mold:
        if a > j or l > j:
            soma = 1
            break
        soma *= j
    delta = soma - (a*l)
    if delta >= 0:
        if delta < menorDelta:
            menorDelta = delta
            melhor = cont


print(melhor)
