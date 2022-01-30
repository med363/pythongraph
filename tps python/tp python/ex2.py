def remplir():
    d={}
    
    n=int(input("nbr d'etudiant: "))
    
    for i in range(1,n+1):
        lE=[]
        nom=input("donner nom: ")
        prenom=input("donner prenom: ")
        while 1:
            try:
                dateNess=int(input('donner date de naissance: '))
                break
            except:
                print("date non valide")
        lE.append(nom)
        lE.append(prenom)
        lE.append(dateNess)
        d[i]=lE
    return d
        


def afficheEtds():
        d=remplir()
        return d
        
        

print(afficheEtds())

def saisieNote():
    lE=[]
    d={}
    n=int(input('nbr de matoer: '))
    for i in range(1,n+1):
        lN=[]
        while y<=0 and y>=20:
            y=int(input("note de matier "))
            break
        coff=int(input("coff  du matier : "))
        lN.append(tuple(y,coff))
        lE.append(lN)
        d[i]=lE
    return d
        
        
        
            
                
        
    