# pour que nbre premier il suffit que les divisseur soit entre 2 et racine de n ((1<sqrt))
from math import sqrt
n=int(input('donner un nbre>0:  '))
def premier(n):
    i=2
    while i<=(sqrt(n)) and n%i!=0:
        i=i+1
    if i>=(sqrt(n)) and n>1:
        print('premier')
    else:
        print('non premier')
        
premier(n)