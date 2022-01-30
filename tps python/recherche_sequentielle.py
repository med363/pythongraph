def rech(t,v):
    position=-1
    i=0
    n=len(t)
    while(i<n and position==-1):
        if t[i]==v:
            position=i
        else:
            i=i+1
    return(position)