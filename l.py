def lectureFichier(): 
    # arcsL=[]
    fich = input("Entrez le nom du fichier de sauvegarde : ")
    ofi = open(fich, "r")
    lines=ofi.readlines()
    
    for line in  lines :  
        #print(line)
        l= line.rstrip('\n').split(":")
        # print(l)
        for e in l[0]:
            print(e[0])
        while 1:
            arcsL=[]
            val=l[1].split("#")
        # val.append(e[0])
            val.insert(0,e[0])
            val = list(map(int, val))
            print(val)
        # val.remove('\n')
            arcsL.append(val)
            
        return arcsL
    
        #print(l)
    ofi.close()
    


lectureFichier()