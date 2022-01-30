


arcs=[]
# def lecture():
#     n=int(input("donner le nbre d'arc :"))
#     while(n<=0):
#         n=int(input("donner le nbre d'arc : "))
#     return n
def remplir():
    # arcs=[]
    # for i in range(1, n+2):
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
            
        return arcs

def enregistrement(): 
    fich = input("Entrez le nom du fichier de sauvegarde : ")
    ofi = open(fich, "w")
 # écriture d'une ligne-repère pour identifier le type de fichier :
    #ofi.write("graph\n")
 # parcours du dictionnaire entier, converti au préalable en une liste :
    for e in arcs:
        li=[]
        li.append(str(e[1]))
        li.append(str(e[2]))
        t=tuple(li)
 
        ch='#'.join(t)
        ch=str(e[0])+":" + ch+'\n'
        ofi.write(ch)
 # utilisation du formatage des chaînes pour créer l'enregistrement :
         #ofi.write("{0}:{1}\n".format(cle, valeur))
    ofi.close() 
    
    
    
def lectureFichier(): 
    arcsL=[]
    fich = input("Entrez le nom du fichier de sauvegarde : ")
    ofi = open(fich, "r")
    lines=ofi.readlines()
    
    for line in  lines :  
        #print(line)
        l= line.rstrip('\n').split(":")
        # print(l)
        for e in l[0]:
            print(e[0])
        val=l[1].split("#")
        # val.append(e[0])
        val.insert(0,e[0])
        val = list(map(int, val))
        print(val)
        # val.remove('\n')
        arcsL.append(val)
            
    print(arcsL)
    
        #print(l)
    ofi.close()
 
        






# from tkinter import *
# from tkinter import ttk
# import tkinter as tk

# # declare title , size et type d'input tkinter
# root = Tk()
# root.title("spannig tree")
# root.geometry("1080x720")
# my_tree = ttk.Treeview(root)
# storeName = "Test SariSari Store"










            



while 1: 
    choix = input("choisisez : (R)emplisatge -  (E)nregistrais - (L)ecture - (K)ruskal -  (T)erminer : ")
    # print(choix)
    if choix.upper() == 'R':
        remplir()
    elif choix.upper() == 'E' : 
        enregistrement() 
    elif choix.upper() == 'L' : 
        lectureFichier()
    elif choix.upper() == 'K' : 
        from kurskal import *
    elif choix.upper() == 'T':
            break      

    