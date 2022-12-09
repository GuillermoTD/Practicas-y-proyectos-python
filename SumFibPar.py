def SumFibPar(n):
    sum = 2
    a=1
    b=2
    p=a+b

    while p < n:
        if p % 2 == 0:
            sum+=p
        a=b
        b=p
        p=a+b
    return sum

print(SumFibPar(4000000))



