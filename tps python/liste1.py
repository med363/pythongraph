l1 = list()
#lecture d'un nbre compris entre entre 1 et 10
def lecture():
    x = int(input("donner un entier :"))
    while  x <1 or x >10:
        x = int(input("donner un entier :"))
    return x
        
#ajout avec une boucle for de n elt
#remplissage d'une liste de n entiers
def remplir(n):
    l = []
    for i in range(1,n+1):
        l.append(int(input("donner une valeur ")))
    return l   
        

#fonction qui permet d'afficher une liste
def afficher(l):
    n = len(l) #retourne la longueur de la liste
    #1ère méthode
    for i in l:
        print(i)
    #2ème méthode
    for i in range(0,n):
        print(l[i])

#calcul du maximm de la liste
def maximum(l):
    max = l[0]
    for i in l:
        if( i > max):
            max = i
    return max
#programme principal


#appel de la fonction lecture
n = lecture()
l = remplir(n)
afficher(l)
m = maximum(l)
print("le maxium de la liste est :", m)
print("le maxium de la liste est :", maximum(l))

