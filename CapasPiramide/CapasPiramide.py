def CapasPiramide(n):
    C = 2
    T = n
    S = T-1
    CU = 4
    while S >= CU:
        S -= CU
        C += 1
        CU = C**2
    print(C-1,S)
  

CapasPiramide(35)
