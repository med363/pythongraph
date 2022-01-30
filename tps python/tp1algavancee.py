# def pui(x,p):
      
#     for i in range(1,p+1):
#         puissance=x**i
#     return puissance
    
# x=float(input("Donner une valeur "))
# p=int(input('Donnez un entier positif '))
    
# print(x,'a la puissance',p,"est egal:",pui(x,p))


# autre methode
# def pui(x,p):
#     puissance = 1
#     for i in range(p):
#         puissance=x*puissance
#     return puissance

# x=float(input("Donner une valeur "))
# p=int(input('Donnez un entier positif '))
    
# print(x,'a la puissance',p,"est egal:",pui(x,p))
   
   
# methode amiliore

# def pui(x,p):
#     for i in range(1,p+1):
#         puissance=x*(x**(p-1))
#     return puissance

# x=float(input("Donner une valeur "))
# p=int(input('Donnez un entier positif '))
    
# print(x,'a la puissance',p,"est egal:",pui(x,p))


# recursive
# def pui(x,p):
#     r = 1
#     if p!=0:
#         if p%2 :
#             c = pui(x,p//2)
#             r=c*c
#         else :
#             c = pui(x,p//2)
#             r=c*c*x
#     return r

def pui(x,p):
    r = 1
    if p!=0:
        c = pui(x,p//2)
        if p%2 :
        
            r=c*c
        else :
            
            r=c*c*x
    return r

x=float(input("Donner une valeur "))
p=int(input('Donnez un entier positif '))
    
print(x,'a la puissance',p,"est egal:",pui(x,p))