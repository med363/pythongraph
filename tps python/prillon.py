# def add(a=1,b=2):
#     z=a+b
#     return z

# def produit(a=1,b=2):
#     z=a*b
#     return z

# print(add(a=1,b=2))
# print(produit(a=1,b=2))


# n=int(input("d"))
# print(diviseurs(n) )   

# saisie()

# n=int(input("donnee  "))
# print(premier(n))
fich = input("Entrez le nom du fichier de sauvegarde : ")
ofi = open(fich, "r")
lines=ofi.readlines()
    
for line in  lines :  
        #print(line)
    l= line.split(":")
    val=l.append("#")
    
print(val)