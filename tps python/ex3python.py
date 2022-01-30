            

def remplirList():
     l=[]
     nom=input("nom: ")
     prenom=input("prenom")
     while 1:
         try:
             dateness=int(input("donner date de naissance: "))
             break
         except:
             print("saisie entier!!")
     l.append(nom)
     l.append(prenom)
     l.append(dateness)
     return l

def remplirDict():
     d={} 
     while 1:
         try:       
           n=int(input("donner nbre d'etds: "))
           break
         except:
             print("saisie entier!!")
        
     for i in range(1,n+1):
          
          
          d[i]=remplirList()
        
            
     return d

print(remplirDict())
# # d=remplirDict()

# # def afficheEtds(d):
# #     for k,v in d.items():
# #         d[k]=v
# #         return d
        
# # print(afficheEtds())

# # def saisieNote(l):
# #     lN=[]
# #     n=int(input(' saisie nb matiere'))
# #     while n<0 and n>=20:
# #         try:
# #             n=int(input("saisie note entre 0 et 20: ")) 
# #             print('note bien saisie')
# #             break
# #         except:
# #             print('err de saisie')
# #         if n not in l:    
# #             lN.append(n)
# #     for k,v in d.items():
# #         if lN not in d.values():
# #             d[k]=lN
        
# # def saisieNote(l):
# #     for i in range(l):
# #         n=int(input("donner le nb matieres "))
# #         ln=[]
# #         for j in range(n):
# #             note=float(input("donner le matiere de matier"))
# #             ln.append(note)
# #         l[i]['notes']=ln
# #     return l
                        
            

# #def saisieNotes():
# #    remplirList()
# #    n=int(input("nbre de matiers"))
   
            
#     # lm=["algo","big data","linux","theorie de language"]       
# #    for i in range(1,n+1) :
# #        ln=[]
#  #       while 1:
# #            try:
            
# #               n1=int(input("donner note compris d'une matiere enttre 0 et 20: "))
# #               if n1<=20 and n1>=0:
# #                   print("a valable note")  
# #               break
           
# #            except :
# #               print("note doit etre entre 0 et 20 !!")
# #        ln.append(n1)
# #        remplirList().append(ln)
# #    return remplirDict()
# # l=remplirList()
# # saisieNote(l)       
        
# #print(saisieNote())
# my_dict=dict()
# def remplir():
#     n=int(input("donner nbre d'etudiant: "))
#     for i in range(1,n+1):
#         l=list()
#         nom=input('nom ')
#         prenom=input('prenom ')
#         date=(input('date de naissance: '))
#         l.append(nom)
#         l.append(prenom)
#         l.append(date)
#         my_dict[i]=l
#     return my_dict

# my_dict=remplir()
# print(my_dict)