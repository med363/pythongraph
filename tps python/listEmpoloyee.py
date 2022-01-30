def ajouEmp():
    l=[]
    n = int(input("Enter number of employee : "))
 
    for i in range(0,n+1):
        Emp = input()
        l.append(Emp)
        
def affchSold(l):
    max=l[0]
    for i in range(0,len(l)+1):
        if l[i] >= max:
            max==print(l[i])
            
            
def somSold(l):
    s=0
    for i in l:
        s=s+i
    return s

def main():
    l=[[12,22635842,'benfolen',"med",1000]]
    