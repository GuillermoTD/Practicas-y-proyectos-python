# Numeros de lychrel en un rango menor de 10,000

def reverso(n:int):
    #reverso de n
    reverso = 0
    while n > 0:
        reverso = reverso*10 + n%10
        n = n//10
        print(reverso)
    return reverso

reverso(123)

def palindro(n:int):
    
    m = 0
    d = 3
    mn = 10**(d-1)
    mx = 10**d-1
    for n in range(mn, mx+1):
        for k in range(n, mx+1):
            p = n*k
            if palindro(p) and p>m:
                m=p
    print(p)




def Lychrel_Function(n):
    flag = 0
    if ():
        pass


Lychrel = 0

t = 10000

for i in range(1, t + 1):
    if Lychrel_Function(i):
        Lychrel +=1

print(Lychrel)
