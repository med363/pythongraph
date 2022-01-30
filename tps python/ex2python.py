def  nbreocc():
    ch=input("donner chaine: ")
    mot=ch.split()
    for i in range(len(mot)):
        n=mot.count(mot[i])
        print(mot[i],n)
    
nbreocc()