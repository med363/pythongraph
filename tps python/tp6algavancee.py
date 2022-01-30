def miroir():
    n=int(input("nomber mimoir: "))
    miroir=0
    while n!=0:
        miroir=(miroir*10)+(n%10)
        n=n//10
    print(f'le miroir de {n} est: ',miroir)

miroir()