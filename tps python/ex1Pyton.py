def remplir(l):
    lPaire=list()
    lImpaire=list()
    for i in l:
        if i%2 == 0 :
            lPaire.append(i)
        else:
            lImpaire.append(i)
    return lPaire,lImpaire
        
l=[2,3,5,9,4,8,10,12,11]
print(remplir(l))

