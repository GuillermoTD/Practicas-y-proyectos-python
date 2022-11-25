import time

def SiDiv(n, t):
    # si n es div por los nat de 1 t
    e = 1
    d = 2
    while e and d < t+1:
        if n % d != 0:
            e = 0
        d += 1
    return e

# Menor # natural divisible por los nat del 1 al 20

t = 20
n = 1
s = 1

i = time.time()

while s:
    if SiDiv(n, t):
        s = 0
        m = n
    n += 1

    f = time.time()

    tin = (f-i)

    print("Tiempo: ", tin, end="\r")

print()
print()

print(m)

print()


