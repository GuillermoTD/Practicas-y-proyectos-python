def Multiple(n):
    # suma de los multiplos de 3 o 5 menores que n.
    sum=0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum+=i
    return sum

print(Multiple(1000))
