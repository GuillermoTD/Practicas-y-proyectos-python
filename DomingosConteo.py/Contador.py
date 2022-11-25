def diaAnterior(dia1,mes1,anio1,dia2,mes2,anio2):
    # isBefore=True
    dia= dia1
    mes= mes1
    anio= anio1

    if(dia1 < dia2 and dia2 < 31):
        dia1 += dia1

    if(mes1 < mes2 and mes2 < 12):
        mes1 += mes1
        
    if(dia1 < mes2 and anio2 < 2000):
        anio1 += anio1

    print(dia,"/",mes,"/",anio)

    dia = int(input("Ingrese el dia "))
    mes = int(input("Ingrese el mes "))
    anio =int(input("Ingrese el anio "))

    dia1 = int(input("Ingrese el dia1  "))
    mes1 = int(input("Ingrese el mes1  "))
    anio1 =int(input("Ingrese el anio1  "))

def Bisiesto(a):
    bisiesto = 0
    if a % 4 == 0:
        bisiesto = 1
        if a % 100 == 0:
            bisiesto = 0
            if a % 400 == 0:
                bisiesto == 1
    return bisiesto

def numDomingos(d1):
    #cantidad de domingos 1ro del siglo 20
    numDom = 0
    if d1 == 1:
        numDom = 1
    return numDom

def diaSiguiente(dia,mes,anio):
    #12/5/1990
    #calcular dia siguiente 
    meses = [31,28,31,30,31,30,30,31,30,31,30,31]
    meses[1]+= Bisiesto(anio)

    dia+=1
    if dia > meses[mes-1]:
        dia = 1
        mes +=1
        if mes > 12:
            mes = 1
            anio +=1
    print(dia,mes,anio)

# ------------------------------Main------------------------------

numDom=0
dia=0
mes=0
anios=0

diaSiguiente(12,6,1984) 


