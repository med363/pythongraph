L=int(input("donner un entier: "))
R=int(input("donner un entier: "))
n=int(input("donner un entier: "))


def impaire(L,R):
    for i in range(L,R+1):
        if i%2!=0 and L<R and i%n!=0:
            print(i)
    
            
            
impaire(L,R)