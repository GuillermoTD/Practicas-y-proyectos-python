#Suma fibos pares menores que 1,000,000

# def proximo(b,p):
    


def SumaFibonacci(n):
    suma=2
    numA=1
    numB=2
    numSiguiente = 3
    while numSiguiente < n:
        if numSiguiente % 2 == 0:
            suma+=numSiguiente
        numA,numB,numSigiuente = proximo(numB,numSiguiente)
    