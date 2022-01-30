#lecture d'un nbre compris entre entre 1 et 10
def lecture():
    x = int(input("donner un entier :"))
    while  x <1 or x >10:
        x = int(input("donner un entier :"))
    return x
def remplir(n):
    listep = []
    
    for i in range (1,n+1):
        l2 = []
        nom = input("donner le nom :")
        pre = input("donner le prénom :")
        solde = int(input("donner son solde :"))

        l2.append(nom)
        l2.append(pre)
        l2.append(solde)
        listep.append(l2)
    return listep
def sommeSolde(l):
    som = 0
    n=len(l)
    for i in range(0,n):
        som = som + l[i][2]
    return som


n = lecture ()
l = remplir(n)
print(l)
s = sommeSolde(l)
print("la somme des soldes est :", s)
        
