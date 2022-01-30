my_dict=dict()
def remplir():
    for i in range(1,4):
        l=list()
        nom=input('nom ')
        prenom=input('prenom ')
        while True:
            try:
                moy=float(input('moyenne: '))
                break
            except:
                print('donne reel!!')
        l.append(nom)
        l.append(prenom)
        l.append(moy)
        my_dict[i]=l
    return my_dict

my_dict=remplir()
print(my_dict)