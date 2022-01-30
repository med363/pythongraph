def remplir():
    arcs=[] #list des arcs

    while 1:
        l=[] #liste d'une arc
        try:    
            somet=int(input('donner somet <ou> taper entree '))
        except ValueError:
            break
        l.append(somet)
        while 1:
            try:
                voisin=int(input('donne voisin: '))
            except ValueError:
                break
            l.append(voisin)
            print('cout de ',somet,'vers',voisin)
            val=int(input())
            l.append(val)
        arcs.append(l)
    print(arcs)
    for i in arcs:
        print(i)
         


remplir()