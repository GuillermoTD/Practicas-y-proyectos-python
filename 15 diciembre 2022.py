def isPrimo(n):
    '''Recibe un entero (n) y determina si este es primo o no'''
    isP = n>1
    ds = 2
    while isP and ds<n:
        if isDivisible(n,ds):
            isP = 0
    return isP
def isDivisible(dd,ds):
    '''Recibe dos numeros enteros, (dd) -> Dividendo y (ds) -> divisor y retorna si dd es divisible entre ds '''
    isD = 0
    if dd%ds == 0:
        isD = 1
    return isD