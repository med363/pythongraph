import json
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 20:52:13 2020

@author: 

"""
def dijkstra(mg,s): 
    #somme de tout les arcs de mon graph +1
    infini = sum(sum(mg[sommet][s2] for s2 in mg[sommet]) for sommet in mg)+1
    #s_connu c'est l'origin dont d[u]=0 et parent de u lui meme ou j'ai stockee la plus court chemin et le parent de u
    s_connu = { s:[0,[s]]}
    #s_iconnu c'est tout les u dont d[u]=00 et le parent de u est egale nil
    s_inconnu = { k : [infini,''] for k in mg if k !=s}
    #pour chaque noeud suivant de u on va change la valeur de nil par son parent 
    for suivant in mg[s]:
        # longeur de l'arc et le noeud u
            s_inconnu[suivant] = [mg[s][suivant], s]
    # affichage du noeud qu'on a traiter et le chemin du branch        
    print("Dans le graphe d'origine {} dans les arcs sont: ".format(s))  
    for k in mg:
        print(k ,":", mg[k])     
    print()      
    print("Plus courts chemins de ")
    #relachement
    # tant que d[u]=00 et parent de u est egale nil 
    while s_inconnu and any(s_inconnu[k][0] < infini for k in s_inconnu):
        #u c'est l'arc le plus courtre chemin à l'origine
        u = min(s_inconnu,key=s_inconnu.get)
        #on recupere le longeur d'arc entre les deux noeuds et le parent de u dans le dictionnaire s_inconnu
        longeur_u,precedent_u = s_inconnu[u]
        #pour chaque suivant de u dans la graph
        for v in mg[u]:
            # si le suivant de u n'est pas etre connu d[v]=00 parent[v]=nil
            if  v in s_inconnu:
                # on calcul d[u] on suppose que u=sommet or d[u]=0 + cout de l'arc de u et son voisin v
                d= longeur_u+mg[u][v]
                #si d plus petit que d[v] puisque intiallement d[v]=00
                if d < s_inconnu[v][0]:
                    #on affecte une lise contient d==> cout et u ==> parent de v
                    s_inconnu[v]= [d,u]
        #on supposse qu'un traite on va la recupere dans le dictionnaire s_connu avec son liste contient longueur d'arc de u et v 
        s_connu[u]=[longeur_u,s_connu[precedent_u][1]+[u]]  
        #on supprime d[u]=00
        del s_inconnu[u]
        #on affiche le plus court chemin de d[u]
        print('longueur',longeur_u,':',' ->'.join(s_connu[u][1]+[v])) 
    #on affiche les noeud qu'on n'a pas suivre
    for k in s_inconnu:
        print("il n'ya au chemain {} a {}".format(s,k))  
    print()     
    return s_connu


#graph = {'A' :(('b','5'),('e','3')),
        # 'B' : (('A','1')),
         #'C' : (('d','5'),('f','8')),
         #'D' : None ,
		 #'E' :(('f','2'),('c','6')),  
         #'f' :(('b','4'))
         #}


def remplisage(): 
    while 1 :
        somet =input("entrer le somet (ou <entrer> pour terminer ) : ")
        if somet =="":
            break
        else:
            while somet in graph.keys():
                 somet =input("Réentntrer le somet (ou <entrer> pour terminer ) : ")
        #saisie des voisin :

        l=[] #liste de voisin
        l1={} #liste de couple(tuple)
        while 1 : 
            
            noued = input("entrer le noued voisin  : ")
            if noued =="":
                break 
            
            elif noued not in l :
                l.append(noued)
                print("donnez la valuer de ", somet, "vers ", noued)
                val=int(input())
                l1[noued]= val
            #ajouter d'un sommet dans le dict graph
        graph[somet]=l1
    print( graph)


def enregistrement(graph): 
    fich = input("Entrez le nom du fichier de sauvegarde : ")
    ofi = open(fich, "w")
    print(graph)
 # écriture d'une ligne-repère pour identifier le type de fichier :
    
 # parcours du dictionnaire entier, converti au préalable en une liste :
        #♠print("l1",l1)
        #l={}
        #d={}
        #for elt in graph.keys(): 
            #l[str(elt)]=l1
 #           l.append(str(elt[1]))
        #print(l)
        #d=l.update(l1)
        
  #      d=cle+":"+d+"\n"
    ch = json.dumps(graph)
    ofi.write(ch)
 # utilisation du formatage des chaînes pour créer l'enregistrement :
         #ofi.write("{0}:{1}\n".format(cle, valeur))
    ofi.close() 
    
#Une fonction qui permet de charger la graph à partir d’un fichier
#Une fonction qui permet de charger la graph à partir d’un fichier
def lectureFichier(): 
    fich = input("Entrez le nom du fichier de sauvegarde : ")
    ofi = open(fich, "r")
    graph={}
    graph=ofi.read()
    print(graph)
#    lines=ofi.readlines()
    
#    for line in  lines :
    # for cle, valeur in graph.items():
    #     l1=valeur
    #     graph[cle]=l1  
    #     #print(line)
#        l= line.split(":")
#        val=l.append("#")
#        graph[val]=l
        #print(l)
    ofi.close() 
    return graph 



graph={}
while 1: 
    choix = input("choisisez : (R)emplisatge -  (E)nregistrais - (L)ecture - (D)dijkstra  (T)erminer : ")
    if choix.upper() == 'R':
        graph=remplisage()
    elif choix.upper() == 'E' : 
        enregistrement(graph)
    elif choix.upper() == 'L' : 
        graph=lectureFichier()
    elif choix.upper() == 'D':
        origine=input("donne l'origine: ")
        dijkstra(graph,origine)
    elif choix.upper() == 'T':
        break    



  
# grapheDisco = {
#   'K':{'M':4,
#        'E':1},
#   'M':{'E':2,
#        'H':2},
#   'E':{'M':1,
#        'H':3,
#        'F':1},
#   'N':{'F':4},
#   'F':{'H':1},
#   'S':{'H':1,
#        'F':2},
  
        
# }
