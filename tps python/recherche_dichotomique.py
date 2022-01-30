def rechercher(t,x):
    n=len(t)
    trouve=False
    debut=0
    fin=len(t)-1
    while (debut<=fin and trouve==False):
        milieu=(debut+fin)//2
        if t[milieu]==x:
            trouve==True
        elif t[milieu]<x:
            debut=milieu+1
        else:
            fin=milieu-1
    if trouve==True:
        return milieu
    else:
        return -1
                
        