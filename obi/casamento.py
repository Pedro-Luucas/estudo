a = int(input())
b = int(input())
astr = str(a)
bstr = str(b)

if len(astr) > len(bstr):
    
    maiorA = True
    while len(astr) > len(bstr):
        bstr = '0' + bstr

    maior = astr
    menor = bstr

if len(bstr) > len(astr):
    
    maiorA = False
    while len(bstr) > len(astr):
        astr = '0' + astr 
    
    maior = bstr
    menor = astr

lsMaior = [x for x in maior]
lsMenor = [x for x in menor]

for i in range(len(maior)):
    if int(lsMaior[i]) > int(lsMenor[i]):
        lsMenor[i] = -1
    if int(lsMaior[i]) < int(lsMenor[i]):
        lsMaior[i] = -1
    if int(lsMaior[i]) == int(lsMenor[i]):
        continue

lsMaior = [x for x in lsMaior if x != -1]
lsMenor = [x for x in lsMenor if x != -1]

maior = ''.join(lsMaior)
menor = ''.join(lsMenor)

if maiorA:
    print(maior, menor)
else:
    print(menor, maior)