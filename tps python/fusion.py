

def fussionner(T,d,m,F):
    T1=[0]*(F-d+1)
    i=d
    j=m+1
    k=0
    while (i<=m and j<=F):
        if(T[i]<=T[j]):
            T1[k]=T[i]
            i=i+1
        else:
            T1[k]=T[j]
            j=j+1
        k+=1
        
        if i<=m:
            T1[k]=T[i]
            i+=1
        else:
            T1[k]=T[j]
            j+=1
            
        j=d
        for i in range (k+1):
            T[j]=T1[i]
            j+=1
        
        
def tri_fusion(T,deb,fin):
    if (deb<fin):
    
        mil=(deb+fin)//2
        tri_fusion(T,deb,mil)
        tri_fusion(T,mil+1,fin)
        fussionner(T,deb,mil,fin)
        
        
# Programme principale pour tester le code ci-dessus
tab = [98, 22, 15, 32, 2, 74, 63, 70]
 
tri_fusion(tab,0,len(tab)-1)
 
print ("Le tableau trié est:")
for i in range(len(tab)):
    print ("%d" %tab[i])