
def occ():
    # ch=input("donner phrase: ")
    # l=[]
    # mot=ch.split()
    # for i in range(len(mot)):
    #     d={}
    #     n=ch.count(mot[i])
    #     d['mot']=mot[i]
    #     d['nbocc']=n
    #     l.append(d)
    #     return l
    d={}
    ch=input("donner une chaine: ")
    mot=ch.split() 
    for i in range(len(mot)):
        n=mot.count(mot[i])
        d[n]=mot[i]
    print(d)

occ()


