# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 19:49:11 2021

@author: DELL
"""

# import tkinter as tk
import os
import time
# from tkinter import *
# from tkinter import ttk
# # delare title , size et type d'input tkinter
# root = Tk()
# root.title("spannig tree")
# root.geometry("1080x720")
# my_tree = ttk.Treeview(root)
# storeName = "Test SariSari Store"




def remplir_switch(switchs,voisin,cost,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de,il_ya_autre_switch):
    while True:
       x=input('donner switch')
       while True:
          switchs.append(x)
          
          ok=input(est_ce_que+" "+str(x)+" "+un_voisin_ou_non +"\n>")
          if(ok=='n' or ok=='ن'):
            cost.append(0)
            voisin.append(" ")
            break
          c=input('donner le voisin')
# switchs   
          voisin.append(c)
          co=input('donner le cout')
          cost.append(co)
       
       ok=input(il_ya_autre_switch+"\n>")
       if(ok=='n'):
           break
    
    return switchs,voisin,cost
    
       
    



def meielleur_route(m_road,m_coast,source,destination):
     rang=0
     e=0
     j=0
     ok=False
     
     while True:
    
      if (m_coast[j]==0  and j<len(m_coast) ):
         j=j+1
      elif (m_coast[j]!=0 and j<len(m_coast)):
          min= m_coast[j]
          ok=True
          break
      else :
         ok=False
         break

     if ok == True :
        while e<len(m_road):
          if m_coast[e]!=0 and m_coast[e]<min:
            min =int( m_coast[e])
            e=e+1
          else:
              e=e+1
        for i in range(len(m_coast)):
                    if(m_coast[i]==min):
                        rang=i
                        break
        return "                le meilleur route de "+str(source)+" ==> "+str(destination)+"  est \n                "+str(m_road[rang]+" le cout est : "+str(m_coast[rang]))
     else:
        return "                le meilleur route de "+str(source)+" ==> "+str(destination)+"  est \n                "+str("il n ya aucun route le coast est : "+str(0))





def cherche(switchs,tar):
 ok=-1
 for i in range(len(switchs)):
    if switchs[i]==tar:
        ok=i
        break
 return ok

def supprimer(switchs,voisin,cost,ci,vo,co):
 for i in range(len(switchs)):
    if switchs[i]==ci:
        switchs.remove(switchs[ci])
        voisin.remove(voisin[vo])
        cost.remove(cost[co])
        print("supprission terminer... ")
        break
 return switchs,voisin,cost



def rec_find_and_count(indice,switchs,voisin,cost,source,destination,arbre,nbcost,s,d,terminer,change_langue,import_travaille,sauvgarder_travaille,trouver_route,remplir_graph,welcome_word,supprimer_switch,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de,il_ya_autre_switch):
   
    if  voisin[int(indice)]==d:
        arbre.append(str(source)+"----->"+str(destination))
        nbcost.append(cost[indice])
        return arbre , nbcost

    
    elif (voisin[int(indice)]!=d and voisin[int(indice)]!=" "):
        cc=cost[int(indice)]
        
        destination=voisin[int(indice)]
        ch=str(source)+"----->"+str(destination)
        source=voisin[indice]
        indice=cherche(switchs,source)
        if indice!=-1:
         
         destination=voisin[int(indice)]
         arbre.append(ch)
         nbcost.append(cc)
         return rec_find_and_count(indice,switchs,voisin,cost,source,destination,arbre,nbcost,s,d,il_ya_autre_switch,terminer,change_langue,import_travaille,sauvgarder_travaille,trouver_route,remplir_graph,welcome_word,supprimer_switch,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de)
        else:
             arbre.clear()
             nbcost.clear()
             return arbre , nbcost
    elif voisin[int(indice)]==" ":   
        
         
        return rec_find_and_count(indice+1,switchs,voisin,cost,source,destination,arbre,nbcost,s,d,il_ya_autre_switch,terminer,change_langue,import_travaille,sauvgarder_travaille,trouver_route,remplir_graph,welcome_word,supprimer_switch,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de)
    else:  
      return arbre , nbcost

def cherche_plus_courte_route(switchs,voisin,arbre,nbcost,cost,terminer,change_langue,import_travaille,sauvgarder_travaille,trouver_route,remplir_graph,welcome_word,supprimer_switch,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de,il_ya_autre_switch):
    
    ch=0
    print("table   switch      : "+str(switchs))
    print("table switch voisin : "+str(voisin))
    print("table coute switch  : "+str(cost))
    if len(switchs)==0:
            switch()
    
    source=input("donner la switch source\n>")
    destination=input("donner la switch destination\n>")
    arbre=[]
    nbcost=[]
    r=[]
    superroad=[]
    supercoast=[]
   #**************************************************************
   
   
    for x in range(len(switchs)):
        if(switchs[x]==source and voisin[x]!=" "):
            r.append(x)
            
    ch1=""
    ch2=0
    s=source
    d=destination
    f=0
    for u in range(len(r)):
      m_road , m_coast = rec_find_and_count(int(r[u]),switchs,voisin,cost,source,destination,arbre,nbcost,s,d,il_ya_autre_switch,terminer,change_langue,import_travaille,sauvgarder_travaille,trouver_route,remplir_graph,welcome_word,supprimer_switch,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de)
      for i in range(len(m_road)):    
         ch1=ch1+m_road[i]
         ch2=ch2+m_coast[i]
      supercoast.append(ch2)
      superroad.append(ch1)
      ch1=""
      ch2=0
      m_road.clear()
      m_coast.clear()
    find=False
    for i in range(len(superroad)):
        if(supercoast[i]!=0):
            find=True
            break
        else:
            find=False
    if (len(superroad)>0 and len(supercoast)>0 and find==True):
       print(meielleur_route(superroad,supercoast,source,destination))
      
    else:
        print("il n ya aucun relation entre "+source+" est "+destination) 
    main_switch(switchs,voisin,arbre,nbcost,cost,terminer,change_langue,import_travaille,sauvgarder_travaille,trouver_route,remplir_graph,welcome_word,supprimer_switch,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de,il_ya_autre_switch)
    
def francais():
    donner_switch="donner switch"
    un_voisin_ou_non="un voisin ou non ? (o/n)"
    est_ce_que="est ce que"
    donner_la_voisin_de="donner la voisin de "
    donner_la_coute_de="donner la coute de "
    terminer="terminer"
    il_ya_autre_switch="il'y a un autre switch(o/n)"
    change_langue="change language"
    import_travaille="ouvrir un fichier"
    sauvgarder_travaille="sauvegarder un travaille"
    trouver_route="envoyer une paquet "
    remplir_graph="remplir un graphe "
    welcome_word="Bien venu a Spanning Tree Script  made with A.A.M(Ameni,Ayoub,med amin)"
    supprimer_switch="supprimer un switch "
    return terminer,change_langue,import_travaille,sauvgarder_travaille,trouver_route,remplir_graph,welcome_word,supprimer_switch,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de,il_ya_autre_switch

def arab():
    
    
    
    donner_switch="اعظيني اسم switch \n>"
    un_voisin_ou_non="عنده جار او لا (ن\لا)   ؟   "
    est_ce_que=" هل   "
    
    donner_la_voisin_de="اعطيني جار "
    donner_la_coute_de="اعطيني تكلفة "
    il_ya_autre_switch="هل هناك switch آخر (ن/لا)"
    supprimer_switch="حذف switch"
    terminer="اغلاق"
    change_langue="تغير اللغة"
    import_travaille="فتح ملف"
    sauvgarder_travaille="تخزين العمل"
    trouver_route="إرسال رسالة"
    remplir_graph="بدء او اضافة switch "
    welcome_word="    صنع من قبل (Ameni,Ayoub,med amine)                    spanning Tree مرحبا بك في سكربت "
    return terminer,change_langue,import_travaille,sauvgarder_travaille,trouver_route,remplir_graph,welcome_word,supprimer_switch,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de,il_ya_autre_switch
    
def main_switch(switchs,voisin,arbre,nbcost,cost,terminer,change_langue,import_travaille,sauvgarder_travaille,trouver_route,remplir_graph,welcome_word,supprimer_switch,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de,il_ya_autre_switch):

    
    print("___________________________________________________________________________________________")
    print(welcome_word)
    print("1)"+remplir_graph)
    print("2)"+trouver_route)
    print("3)"+sauvgarder_travaille) 
    print("4)"+import_travaille)
    print("5)"+supprimer_switch)
    print("6)"+change_langue)
    print("7)"+terminer)
    x=input(">")
    if(x == "1" or x=="1)"):
        os.system("cls")
        switchs,voisin,cost =remplir_switch(switchs,voisin,cost,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de,il_ya_autre_switch)
        os.system("cls")
        main_switch(switchs,voisin,arbre,nbcost,cost,terminer,change_langue,import_travaille,sauvgarder_travaille,trouver_route,remplir_graph,welcome_word,supprimer_switch,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de,il_ya_autre_switch)
    elif(x == "2" or x=="2)"):
         cherche_plus_courte_route(switchs,voisin,nbcost,arbre,cost,terminer,change_langue,import_travaille,sauvgarder_travaille,trouver_route,remplir_graph,welcome_word,supprimer_switch,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de,il_ya_autre_switch)
    elif(x == "3" or x == "3)"):
        print(len(switchs))
        for i in range(0,len(switchs)):

         file=open("switch.txt","a")
         file1=open("voisin_switch.txt","a")
         file2=open("cost_switch.txt","a")            

         file.write(switchs[i]+"\n")
         file1.write(voisin[i]+"\n")
         file2.write(str(cost[i])+"\n")
         
         file.close()
         file1.close()
         file2.close()
        os.system("cls")
        print("sauvegarder terminer ...")
        main_switch(switchs,voisin,arbre,nbcost,cost,terminer,change_langue,import_travaille,sauvgarder_travaille,trouver_route,remplir_graph,welcome_word,supprimer_switch,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de,il_ya_autre_switch)
         
    elif(x == "4" or x=="4)"):
        switchs.clear()
        voisin.clear()
        cost.clear()
        file=open("switch.txt","r")
        file1=open("voisin_switch.txt","r")
        file2=open("cost_switch.txt","r")
        for i in file:
         ch=file.readline()
         ch=ch.replace("\n","")
         switchs.append(ch)
         ch1=file1.readline()
         ch1=ch1.replace("\n","")
         voisin.append(ch1)
         ch2=file2.readline()
         ch2=ch2.replace("\n","")
         cost.append(int(ch2))
         
        file.close()
        file1.close()
        file2.close()
        print("loading complet ...")
        
        print(switchs)
        print(voisin)
        print(cost)
        # os.system("cls")
        main_switch(switchs,voisin,arbre,nbcost,cost,terminer,change_langue,import_travaille,sauvgarder_travaille,trouver_route,remplir_graph,welcome_word,supprimer_switch,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de,il_ya_autre_switch)

     
    elif (x == "5" or x=="5)"):
         print("deleting switch complet... ")
         print("table   switch       : "+str(switchs))
         print("table switch  voisin : "+str(voisin))
         print("table cout de switch : "+str(cost))
         efface=input(("Donner le nom de switch pour effacer \n>"))
         while True:
                 i=cherche(switchs,efface)
                 if i !=-1:
                   switchs.remove(switchs[i])
                   voisin.remove(voisin[i])
                   cost.remove(cost[i])
                 else:
                     break
         print("deleting complited ")
         print("table   switch      : "+str(switchs))
         print("table switch voisin : "+str(voisin))
         print("table cout   switch : "+str(cost))
         os.system("cls")
         main_switch(switchs,voisin,arbre,nbcost,cost,terminer,change_langue,import_travaille,sauvgarder_travaille,trouver_route,remplir_graph,welcome_word,supprimer_switch,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de,il_ya_autre_switch)

    elif (x == "6" or x=="6)"):
        print("1)arabic")
        print("2)Francer")
        lang=input("\n>")
        if(lang=="1"):
            terminer,change_langue,import_travaille,sauvgarder_travaille,trouver_route,remplir_graph,welcome_word,supprimer_switch,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de,il_ya_autre_switch=arab()
            main_switch(switchs,voisin,arbre,nbcost,cost,terminer,change_langue,import_travaille,sauvgarder_travaille,trouver_route,remplir_graph,welcome_word,supprimer_switch,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de,il_ya_autre_switch)
            
        elif(lang=="2"):
            terminer,change_langue,import_travaille,sauvgarder_travaille,trouver_route,remplir_graph,welcome_word,supprimer_switch,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de,il_ya_autre_switch=francais()
            main_switch(switchs,voisin,arbre,nbcost,cost,terminer,change_langue,import_travaille,sauvgarder_travaille,trouver_route,remplir_graph,welcome_word,supprimer_switch,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de,il_ya_autre_switch)
        else:
            print("not exist caractere")
            main_switch(switchs,voisin,arbre,nbcost,cost,terminer,change_langue,import_travaille,sauvgarder_travaille,trouver_route,remplir_graph,welcome_word,supprimer_switch,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de,il_ya_autre_switch)
        os.system("cls")
    else:
         os.system("exit")



def Banner():
    print("|      switch 1  |                                   |      switch2   |")
    print("|                |                                   |                |")
    print("|****************|                                   |****************|")
    print("|   --------->   |-----------------|-----------------|   --------->   |")
    print("|                |                 |                 |                |")
    print("|   <----------  |                 |                 |   <----------  |")
    print("|****************|                 |                 |****************|")
    print("                                   |")
    print("                                   |")
    print("                                   |")
    print("                                   |                             ")
    print("|      switch 3  |                 |                 |      switch 4  |")
    print("|                |                 |                 |                |")
    print("|****************|                 |                 |****************|")
    print("|   --------->   |-----------------|-----------------|   --------->   |")
    print("|                |                                   |                |")
    print("|   <----------  |                                   |   <----------  |")
    print("|                |                                   |                |")
    print("|****************|                                   |****************|")
    time.sleep(1)
    os.system("cls")
    print("|      switch 1  |                                   |      switch2   |")
    print("|                |                                   |                |")
    print("|****************|                                   |****************|")
    print("|   <---------   |--S--------------|--------------P--|   <---------   |")
    print("|                |                 |                 |                |")
    print("|   ---------->  |                 |                 |   ---------->  |")
    print("|****************|                 |                 |****************|")
    print("                                   |")
    print("                                   |")
    print("                                   |")
    print("                                   |                             ")
    print("|      switch 3  |                 |                 |      switch 4  |")
    print("|                |                 |                 |                |")
    print("|****************|                 |                 |****************|")
    print("|   <---------   |--T--------------|--------------E--|   <---------   |")
    print("|                |                                   |                |")
    print("|   ---------->  |                                   |   ---------->  |")
    print("|                |                                   |                |")
    print("|****************|                                   |****************|")
    time.sleep(1)
    os.system("cls")
    print("|                |                                   |                |")
    print("|****************|                                   |****************|")
    print("|   --------->   |----------S------|------P----------|   --------->   |")
    print("|                |                 |                 |                |")
    print("|   <----------  |                 |                 |   <----------  |")
    print("|****************|                 |                 |****************|")
    print("                                   |")
    print("                                   |")
    print("                                   |")
    print("                                   |                             ")
    print("|      switch 3  |                 |                 |      switch 4  |")
    print("|                |                 |                 |                |")
    print("|****************|                 |                 |****************|")
    print("|   --------->   |----------T------|------E----------|   --------->   |")
    print("|                |                                   |                |")
    print("|   <----------  |                                   |   <----------  |")
    print("|                |                                   |                |")
    print("|****************|                                   |****************|")
    time.sleep(1)
    os.system("cls")
    print("|      switch 1  |                                   |      switch2   |")
    print("|                |                                   |                |")
    print("|****************|                                   |****************|")
    print("|   <---------   |-----------------|-----------------|   <---------   |")
    print("|                |                 |                 |                |")
    print("|   ---------->  |                 SP                |   ---------->  |")
    print("|****************|                 |                 |****************|")
    print("                                   |")
    print("                                   |")
    print("                                   |")
    print("                                   |                             ")
    print("|      switch 3  |                 TE                |      switch 4  |")
    print("|                |                 |                 |                |")
    print("|****************|                 |                 |****************|")
    print("|   <---------   |-----------------|-----------------|   <---------   |")
    print("|                |                                   |                |")
    print("|   ---------->  |                                   |   ---------->  |")
    print("|                |                                   |                |")
    print("|****************|                                   |****************|")
    time.sleep(1)
    os.system("cls")
    print("|                |                                   |                |")
    print("|****************|                                   |****************|")
    print("|   --------->   |-----------------|-----------------|   --------->   |")
    print("|                |                 |                 |                |")
    print("|   <----------  |                 |                 |   <----------  |")
    print("|****************|                 |                 |****************|")
    print("                                   |")
    print("                      ~~~~~~~~~~~ SPTE ~~~~~~~~")
    print("                                   |")
    print("                                   |                             ")
    print("|      switch 3  |                 |                 |      switch 4  |")
    print("|                |                 |                 |                |")
    print("|****************|                 |                 |****************|")
    print("|   --------->   |-----------------|-----------------|   --------->   |")
    print("|                |                                   |                |")
    print("|   <----------  |                                   |   <----------  |")
    print("|                |                                   |                |")
    print("|****************|                                   |****************|")
    time.sleep(1)
    os.system("cls")
    print("|      switch 1  |                                   |      switch2   |")
    print("|                |                                   |                |")
    print("|****************|                                   |****************|")
    print("|   <---------   |-----------------|-----------------|   <---------   |")
    print("|                |                 |                 |                |")
    print("|   ---------->  |                                   |   ---------->  |")
    print("|****************|                                   |****************|")
    print("                                    ")
    print("                                    ")
    print("                                  SPTE")
    print("                                                                ")
    print("|      switch 3  |                                   |      switch 4  |")
    print("|                |                                   |                |")
    print("|****************|                 |                 |****************|")
    print("|   <---------   |-----------------|-----------------|   <---------   |")
    print("|                |                                   |                |")
    print("|   ---------->  |                                   |   ---------->  |")
    print("|                |                                   |                |")
    print("|****************|                                   |****************|")
    time.sleep(1)
    os.system("cls")
    print("|                |                                   |                |")
    print("|****************|                                   |****************|")
    print("|   --------->   |--------                   --------|   --------->   |")
    print("|                |                                   |                |")
    print("|   <----------  |                                   |   <----------  |")
    print("|****************|                                   |****************|")
    print("                                    ")
    print("                                 SPTE ")
    print("                                   ")
    print("                                                                ")
    print("|      switch 3  |                                   |      switch 4  |")
    print("|                |                                   |                |")
    print("|****************|                                   |****************|")
    print("|   --------->   |-------                     -------|   --------->   |")
    print("|                |                                   |                |")
    print("|   <----------  |                                   |   <----------  |")
    print("|                |                                   |                |")
    print("|****************|                                   |****************|")
    time.sleep(1)
    os.system("cls")
    print("|      switch 1                                             switch2   |")
    print("|                                                                     |")
    print("|************                                             ************|")
    print("|   <--------                                             ---------   |")
    print("|                                                                     |")
    print("|   ---------                                             --------->  |")
    print("|************                                             ************|")
    print("                                    ")
    print("                                    ")
    print("                                  SPTE")
    print("                                                                ")
    print("|      switch 3                                             switch 4  |")
    print("|                                                                     |")
    print("|************                                               **********|")
    print("|   <--------                                               -------   |")
    print("|                                                                     |")
    print("|   ---------                                               ------->  |")
    print("|                                                                     |")
    print("|************                                               **********|")
    time.sleep(1)
    os.system("cls")
    print("|                                                                     |")
    print("|                                                                     |")
    print("|                                                                     |")
    print("|                                                                     |")
    print("|                                                                     |")
    print("|                                                                     |")
    print("                                    ")
    print("                                 SPTE ")
    print("                                   ")
    print("                                                                ")
    print("|                                                                     |")
    print("|                                                                     |")
    print("|                                                                     |")
    print("|                                                                     |")
    print("|                                                                     |")
    print("|                                                                     |")
    print("|                                                                     |")
    print("|                                                                     |")
    time.sleep(1)
    os.system("cls")
     
    print("                                S.P.T.E")
    print("                             SPanning TreE")
    time.sleep(1)
    os.system("cls")
    time.sleep(1)
    print("                                S.P.T.E")
    print("                             SPanning TreE")
    time.sleep(1)
    os.system("cls")
    time.sleep(1)
    print("                                S.P.T.E")
    print("                             SPanning TreE")
    time.sleep(1)
    os.system("cls")
    time.sleep(1)
    print("                                S.P.T.E")
    print("                             SPanning TreE")
    time.sleep(1)
    os.system("cls")
    time.sleep(1)
    print("                                S.P.T.E")
    print("                             SPanning TreE")
    time.sleep(1)
    os.system("cls")
    time.sleep(1)
    print("                                S.P.T.E")
    print("                             SPanning TreE")















def switch():
    Banner()
    switchs=[]
    voisin=[]
    nbcost=[]
    arbre=[]
    cost=[]
    donner_switch="donner switch"
    un_voisin_ou_non="un voisin ou non ? (o/n)"
    est_ce_que="est ce que"
    donner_la_voisin_de="donner la voisin de "
    donner_la_coute_de="donner la coute de "
    terminer="terminer"
    change_langue="change language"
    import_travaille="ouvrir un fichier"
    sauvgarder_travaille="sauvegarder un travaille"
    trouver_route="envoyer un paquet "
    remplir_graph="remplir un graphe "
    il_ya_autre_switch="il ya un autre switch (o/n) "
    welcome_word="Bien venu a Spanning Tree Script  made with A.A.A(Ameni,Ayoub,Amine)"
    supprimer_switch="supprimer un switch "
    main_switch(switchs,voisin,arbre,nbcost,cost,terminer,change_langue,import_travaille,sauvgarder_travaille,trouver_route,remplir_graph,welcome_word,supprimer_switch,donner_switch,un_voisin_ou_non,est_ce_que,donner_la_voisin_de,donner_la_coute_de,il_ya_autre_switch)
# label of input
# switchLabel = Label(root, text="switch", font=('Arial bold', 15))
# QuestionLabel=Label(root,text='Est que il avait un voisin?',font=('Arial bold', 15))
# voisinLabel = Label(root, text="voisin", font=('Arial bold', 15))
# coutLabel = Label(root, text="cout", font=('Arial bold', 15))
# switchLabel.grid(row=1, column=0, padx=10, pady=10)
# QuestionLabel.grid(row=2, column=0, padx=10, pady=10)
# voisinLabel.grid(row=4, column=0, padx=10, pady=10)
# coutLabel.grid(row=5, column=0, padx=10, pady=10)
# # type of input
# entrySwitch = Entry(root, width=25, bd=5, font=('Arial bold', 15))
# entryVoisin = Entry(root, width=25, bd=5, font=('Arial bold', 15))
# entryCout = Entry(root, width=25, bd=5, font=('Arial bold', 15))
# entrySwitch.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
# entryVoisin.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
# entryCout.grid(row=5, column=0, columnspan=3, padx=5, pady=5)
# # buttom of question
# # def switchButtonState():
# #     if (buttonNON['state'] == tk.NORMAL):
# #         buttonNON['state'] = tk.DISABLED
# #     else:
# #         buttonNON['state'] = tk.NORMAL
# buttonOUI = Button(
#     root, text="Oui", padx=5, pady=5, width=10,
#     bd=3, font=('Arial', 15), bg="#0099ff",)
# buttonOUI.grid(row=3, column=0, columnspan=1)
# buttonNON = Button(
#     root, text="Non", padx=5, pady=5, width=10,
#     bd=3, font=('Arial', 15), bg="#e62e00", )
# buttonNON.grid(row=3, column=1, columnspan=1)
# # buttonOUI = tk.Button(root, text="Python Button 1",
# #                     state=tk.DISABLED)
# # buttonNON = tk.Button(root, text="EN/DISABLE Button 1",
# #                     command = switchButtonState)
# # buttonOUI.pack(side=tk.LEFT)
# # buttonNON.pack(side=tk.RIGHT)
# # buttom remplir
# buttonEnter = Button(
#     root, text="remplir la topologie", padx=5, pady=5, width=30,
#     bd=3, font=('Arial', 15), bg="#0099ff")
# buttonEnter.grid(row=6, column=0, columnspan=1)
# # button update
# # buttonUpdate = Button(
# #     root, text="Update", padx=5, pady=5, width=5,
# #     bd=3, font=('Arial', 15), bg="#ffff00", command=)
# # buttonUpdate.grid(row=5, column=2, columnspan=1)
# # button delete
# buttonDelete = Button(
#     root, text="supprimer un commutateur", padx=5, pady=5, width=30,
#     bd=3, font=('Arial', 15), bg="#e62e00")
# buttonDelete.grid(row=6, column=1, columnspan=1)

switch()    

# root.mainloop()