
from math import sqrt

def saisie():
    x=int(input("donner un entier positive "))
    
    while x<=0:
        x=int(input("donner un entier positive "))
    return x
      
        
def diviseurs(n):
    i = 1
    while (i<=0):
        if(n%i==0):
            print('',i)
       
    i=i+1
    
    


def premier(n):
    i=2
    while(i<=n//2):
        if(n%i==0): 
            break
        i=i+1
    if (n%i ==0):
        print(f"{n} n'est pas premier")
    else:
        print(f"{n} est premier")
        
        
n=saisie()
print(f"les diviseurs de {n} ",diviseurs(n))
print(f"est ce que nbre {n} est ",premier(n))

