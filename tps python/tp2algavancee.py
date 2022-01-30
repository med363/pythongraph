from math import sqrt
def diviseurs(n):
    som = 0
    for i in range(1,(n//2)+1):
        if n%i == 0 :
            som=som + i
            
    return som


# autre methode

# *def diviseurs(n):
#     som = 1
#     q = int(sqrt(n)+1)
#     for i in range(1,q):
#         if n%i == 0 :
#             som=som + i +n//i
            
#     return som

# print(diviseurs(220))

def verif():
    
    for i in range(1,100001):
        for j in range(1,100001):
            if diviseurs(i) == diviseurs(j) :
                return print("le couplée est amie")
            else:
                return print("le couplée non amie")
        
verif()


