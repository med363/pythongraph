# def remplisage(): 
#     l1=[]
#     while 1 :
#         somet1 =input("entrer le somet1 (ou <entrer> pour terminer ) : ")
#         if somet1 =="":
#             break
#         l1.append(somet1)  
#         # else:
#         #     while somet in graph.keys():
#         #          somet =input("Réentntrer le somet (ou <entrer> pour terminer ) : ")
#         #saisie des voisin :

#         l2=[] #liste de voisin
#         l3=[] #liste de poids
#         while 1 : 
            
#             noued = input("entrer le noued voisin  : ")
#             if noued =="":
#                 break 
            
#             elif noued not in l2 :
#                 l2.append(noued)
#                 print("donnez la valuer de ", somet1, "vers ", noued)
#                 val=int(input())
#                 l3.append(val)
#             #ajouter d'un sommet dans le dict graph
    
#             listesDeTuples=list(zip(l1,l2,l3))
#     print( listesDeTuples)

    
# remplisage()



# def remplir():
#     l1=[]
#     l2=[]
#     l3=[]
    
#     while 1:
#         somet1=input("s: ")
#         if somet1=='':
#             break
#         l1.append(somet1)
#     while 1:
#         somet2=input("s: ")
#         if somet2=='':
#             break
#         l2.append(somet2)
#     while 1:
#         print("donnez la valuer de ", somet1, "vers ", somet2)
#         val=int(input())
#         l3.append(val)
#     listesDeTuples=list(zip(l1,l2,l3))
#     print( listesDeTuples)

        
# remplir()
def remplir():
    l1=[]
    l2=[]
    l3=[]
    while 1:
        n1=input('donner n1')
        if n1=="":
            break
        l1.append(n1)
        n2=input('donner n2: ')
        if n2=="":
            break
        elif n2 not in l3:
            l2.append(n2)
            print("donnez la valuer de ", n1, "vers ", n2)
            val=int(input())
            l3.append(val)
        arcs=list(zip(l1,l2,l3))
    print(arcs )        
            
            
            
remplir()