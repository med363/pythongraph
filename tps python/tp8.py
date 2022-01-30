from random import *
def tab_alea(n):
    T=[None]*n
    for i in range(n):
        T[i]=randrange(1,9)
    return T

# tri par selection
def tri_selection(tab):
    
   for i in range(len(tab)):

      # Trouver le min
       min = i

       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j
                
       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp

   return tab

# tri à bulle

def tri_bulle(T):
    n=len(T)
    per=True
    while per==True:
        per=False
        for i in range(0,n-1):
            if T[i]>T[i+1]:
                aux=T[i]
                T[i]=T[i+1]
                T[i+1]=aux
                per=True
        n=n-1
        
# prog principale
tab1=tab_alea(5)
print("le tableau non trie : \t",tab1)
# tri a tri_bulle
tri_bulle(tab1)
print("le tab trie \t",tab1)    
# tri par tri_selection
tri_selection(tab1)
print("le tab trie \t",tab1)    