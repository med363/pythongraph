#arcs=[]
def lecture():
    n=int(input("donner le nbre d'arc :"))
    while(n<=0):
        n=int(input("donner le nbre d'arc : "))
    return n
def remplir(n):
    arcs=[]
    for i in range(1, n+2):
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
            break 
    return arcs

# def enregistrement(): 
#     fich = input("Entrez le nom du fichier de sauvegarde : ")
#     ofi = open(fich, "w")
#     for e in arcs:
#         li=[]
#         li.append(str(e[1]))
#         li.append(str(e[2]))
#         t=tuple(li)
#         ch='#'.join(t)
#         ch=str(e[0])+":" + ch+'\n'
#         ofi.write(ch)
#     ofi.close() 
    
    
    
# def lectureFichier(): 
#     arcsL=[]
#     fich = input("Entrez le nom du fichier de sauvegarde : ")
#     ofi = open(fich, "r")
#     lines=ofi.readlines()
    
#     for line in  lines :  
#         #print(line)
#         l= line.rstrip('\n').split(":")
#         # print(l)
#         for e in l[0]:
#             print(e[0])
#         val=l[1].split("#")
#         # val.append(e[0])
#         val.insert(0,e[0])
#         val = list(map(int, val))
#         print(val)
#         # val.remove('\n')
#         arcsL.append(val)
#     print(arcsL)
#     ofi.close()
 
def find(graph,node):
    if graph[node]<0:
        return node
    else:
        temp= find(graph,graph[node])
        graph[node]= temp
        return temp

def union(graph,a,b,answer):
    ta=a
    tb=b
    a= find(graph,a)
    b=find(graph,b)
    if a==b:
        pass
    else:
        answer.append([ta,tb])
    if graph[a]<graph[b]:
        graph[a]+=graph[b]
        graph[b]=a
    else:
        graph[b]=graph[a]+graph[b]
        graph[a]=b

n=lecture()            

answer=[]
ipt=remplir(n)
print(ipt)
ipt=sorted(ipt,key=lambda ipt:ipt[2])
graph=[-1]*(n+1)
for u,v,d in ipt:    
    union(graph,u,v,answer)
print('arbre recouvrant de poids minimum (ARPM) ou arbre couvrant minimum (ACM) dans un graphe connexe non-orienté et pondéré.')
for item in answer:
    print(item) 

    