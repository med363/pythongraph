ipt=[[1,2,1],[1,3,3],[2,6,4],[3,6,2],[3,4,1],[4,5,5],[6,5,6],[7,5,7]]
n=7
ipt=sorted(ipt,key=lambda ipt:ipt[2]) # trie les arcs du graph a partir de cout (position 2 dans la liste) d'une façon croisant
graph=[-1]*(n+1) #
print(graph) 