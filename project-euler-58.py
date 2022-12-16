def isPrimo(n):
    # Determinar si es primo
    p = 1

    # for i in range(2,n): este es el primer caso
    #     if n%i == 0:
    #         pi = 0
    # return pi

    # if n == 1: Este es el segundo caso
    #     p = 0
    # else:
    #     d = 2
    #     while p and d < n:
    #         if n % d == 0:
    #             p = 0
    #         d += 1
    # return p

    if n <= 1:
        p = 0
    elif n == 2:
        p = 1
    else:
        r = n**(0.5)+1
        d = 2
        while p and d < r:
            if n % d == 0:
                p=0
            d+=1
    return p   

diagonals = 1 
Base = 1
primos = 0
ite = 2
porcentaje = 1.0
canDiagonals = 1
Flag = 1

while Flag:
    for i in range(4):
        diagonals += ite

        if isPrimo(diagonals):
            primos += 1

    ite += 2

    canDiagonals += 4

    porcentaje =  (primos / canDiagonals)
    
    print(f"Primos: {primos}",f"Diagonales: {canDiagonals}", f"Base: {Base}", f"Porcentaje: {porcentaje}", end="\r")

    Base += 2

    if (porcentaje < 0.1):
            Flag = 0

print(diagonals)
