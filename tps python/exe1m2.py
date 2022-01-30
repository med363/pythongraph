ch1 = input('donner une 1ère chaîne :')
#l = [] #création de la liste l = list()
chi =''

for c in ch1:
    if c not in chi:
        chi = chi + c #ajouter à la fin de la liste
print(ch1)
print(chi)

ch2 = input('donner une 2ème chaîne : ')
for c in chi:
    print(c ,' existe ', ch2.count(c))
