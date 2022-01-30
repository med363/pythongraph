from math import sqrt

def Rest(x,y):
   return x%y    

# x=int(input("donne un entier positif "))
# y=int(input("donne un entier positif "))
# print(Rest(x,y))


def estPremier(n):
    x=2
    z=int(sqrt(n))
    
    while x<=z and Rest(n,x)!=0:
        x=x+1
    if x>z and x>1:
        return True
    else:
        return False
        
        
        
    #     i%=n
    #     if i%n>x and i%n>=(z-1):
            
    #         print ("nbre non premier")
    #         break;
        
    # print('nbre  premier')
       
    


        
def __main__():

    for i in range(1,101):
        if estPremier(i)==True:
            print(i)
    
__main__()