def lecture():
    n=int(input("donner le nbre d'employés :"))
    while(n<=0):
        n=int(input("donner le nbre d'employés : "))
    return n
def remplir(n):
    lEmp=[]
    for i in range(1, n+1):
        l=[]
        while 1:
            try:
                code = int(input("donner le code l'employé :"))
                break
            except:
                print("erreur de saisie :!!!!")
            
        nompre = input("donner le prénom et le nom de l'employé :")
        solde = float(input("donner le solde de l'emloyé :"))
        l.append(code)
        l.append(nompre)
        l.append(solde)
        lEmp.append(l)
    return lEmp
def plus_Grand_Solde(n, l):
    maxS =l[0][2]#
    for i in range(0,n):
        if (l[i][2] > maxS):
            maxS = l[i][2]
    return maxS
def somme_solde(n, l):
    s=0
    for i in range(0,n):
        s= s+l[i][2]
    return s
    

    
n= lecture()
listeEmp = remplir(n)
print(listeEmp)
print("le solde le plus grand est ", plus_Grand_Solde(n, listeEmp))
print("la somme des soldes des employés est :", somme_solde(n,listeEmp ))



        
