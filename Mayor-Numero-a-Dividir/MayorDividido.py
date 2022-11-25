def dividir(j,k):

    for j in range(k, 6):
        if j % k == 0:
            return True


def MayorDividido(n):
    # Mostrar cual es el menor numero que puede ser dividido por cada uno de los numeros del 1 al 20
    nm = 0
    sum = 0
    for k in range(1, 6):
        if dividir(j,k):
            sum += j
            print(sum)


MayorDividido(10)
