            
class EnsembleDisjoint:
    """
    Cette classe permet de gérer les ensmebles disjoints. Deux éléments sont
    considérés dans le même ensemble s'ils ont le même parent.
    """
    parent = {}

    # Création de n ensemble disjoints, état de départt de notre graphe
    # chaque sommet et c'est le parent de lui meme
    def __init__(self, N):
        for i in range(N):
            self.parent[i] = i

    # Fonction qui permet de retrouver le parent le plus lointain
    def get_parent(self, k):
        # si sommet est le parent de lui meme
        if self.parent[k] == k:
            return k
# sinon on affecte parent du sommet succeseur
        return self.get_parent(self.parent[k])

    # Union de deux ensembles jusque là disjoints
    def Union(self, a, b):
        # on recupere les parents de deux sommets 
        x = self.get_parent(a)
        y = self.get_parent(b)
# on met l'un des parents le parents de l'autre
        self.parent[x] = y

def Kruskal(arcs, nombre_sommets):
    """
    Construction de l'arbre couvrant minimum à l'aide de l'algorithme de Kruskal
    Les paramètres sont :
        - Les arcs du graphe au format (début, fin, longueur)
        - Le nombre de sommets dans le graph
    """
# une liste va contenir l'arbre minimum
    Arbre_minimum = []
    # une classe EnsembleDisjoint
    ed = EnsembleDisjoint(nombre_sommets)
    # pour parcouris tous les <> arcs
    index = 0
# nbre de chemin min pour relie les sommets
    while len(Arbre_minimum) != nombre_sommets - 1:
    #    recuper l'arcs  
        (src, dest, weight) = arcs[index]
        # l'arcs suivant
        index = index + 1
# chercher les parent de sorce et destination de mon arc 
        x = ed.get_parent(src)
        y = ed.get_parent(dest)
#  si le parent de ces deux sommets ne sont pas les memes
        if x != y:
            Arbre_minimum.append((src, dest, weight))
            ed.Union(x, y)

    return Arbre_minimum


if __name__ == '__main__':

    # Liste des arcs au format (début, fin, longueur)
    arcs=[
        ('A','B',2),('A','C',2),('C','B',4)
    ]
    print(arcs)
# la fonction lambda triee un tuple selon la 2eme argument
    arcs.sort(key=lambda x: x[2])
    nombre_sommets = 7
# la fct kursal avoir en parametre les arcs triee de min jusqu'a le max selon 2eme argument et nbre de sommets 
    print(Kruskal(arcs, nombre_sommets))
