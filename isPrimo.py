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


for i in range(1, 100):
    if isPrimo(i):
        print(i, end=' ')
