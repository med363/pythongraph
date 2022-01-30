def fusion(T,d,m,f):
    T1=[0]*(f-d+1)
    i=d
    j=m+1
    k=0
    while (i<=m and j<=f):
        if (T[i]<=T[j]):
            T1[k]=T[i]
            i=i+1
        else:
            T1[k]=T[j]
            j=j+1
        k+=1
        
    if i<=m:
        T1[k]=T[i]
    else:
        T1[k]=T[j]
    j=d
    for i in range(k+1):
        T[j]=T1[i]
        j=j+1
    print(T)

def tri_fusion(T,d,f):
    if(d<f):
        m=(d+f)//2
        tri_fusion(T,d,m)
        tri_fusion(T,m+1,f)
        fusion(T,d,m,f)

 
T= [98, 22, 15, 32, 2, 74, 63, 70]

tri_fusion(T,0,7)
print ("Le tableau trié est :")
print(T)
