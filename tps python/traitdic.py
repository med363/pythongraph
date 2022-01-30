def lecture():
    x = int(input("donner un entier :"))
    while  x <1 or x >10:
        x = int(input("donner un entier :"))
    return x
def remplir(n):
    d = dict() # d={}
    for i in range (1,n+1):
        l2 = []
        code = int(input("donner le code :"))
        nom = input("donner le nom :")
        pre = input("donner le prénom :")
        solde = int(input("donner son solde :"))
        l2.append(nom)
        l2.append(pre)
        l2.append(solde)
        d[code]=l2
        
        
        
    return d
n = lecture()
d= remplir(n)
print(d)
