while True:
        try:
            N=int(input("donner taille du tab :"))
        except:
            print('donnée doit etre numerique')
        else:
            break
        

T=[None]*N
for i in range (N):
    while True:
        try:
            T[i]=int(input("Donner la valeur de i: "))
        except:
            print('donnée doit etre numerique')
        else:
            break
    max=T[0]
    for i in range(len(T)):
        if T[i] >= max:
            max=T[i]
print(max)