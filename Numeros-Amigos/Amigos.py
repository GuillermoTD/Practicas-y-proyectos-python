def sumaFactores(n):
    # Funcion que determina si un numero m es 
    s = 0
    for d in range(1, n//2+1):
        if not n % d:
            s = s+d
    return s

def Amigo(n):
    am = 0
    b = sumaFactores(n)
    a = sumaFactores(b)
    if n == a and b != a:
        am = b
    return am

# suma de los #s amigos < 10000
s = 0
t = 10000

for n in range(1, t):
    b = Amigo(n)
    if b and b < t:
        s += n
        print(b)
print(s)
