# def R1(n):
#     if (n <= 0):
#         return 1
#     else:
#         return 2 * R1(n-1)
def R2(n):
    if (n <= 0):
        return 1
    else:
        return R2(n-1) + R2(n-1)
n=int(input("d: "))
print(R2(n))