D=3
print(type(D))
# sensible à la case
X="bonjour"
print(X)
X="med amine blibech"
print(X)
# affiche format
c = 24
nom = "Amine"
print(f"{nom} a {c} ans")
print("{} a {} ans".format(nom,c))
p=3.5442428
print(f"ecrire un nombre reel {p:.1f}")
print(f"ecrire un nombre reel 2 chiffre apres le vercule {p:.3}")
# permutation
A=5
B=6
A,B=B,A
print("A est egal",A,"B est egal",B)
# point fort print list ou bien dictionnaire
list=[1,2,3]
print(list)
print(list[1])
# saisie des enties et float pour faire la somme
z=int(input("donner un entier: "))
m=int(input("donner un entier: "))
e=float(input("donner un reel: "))
som=z+e
# division entier
div=z//m
division=z/e
mod=z%m
print(som,div,division,mod)
