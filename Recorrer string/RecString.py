def ObtenerString(string):
    espacio=0
    palabra=0
    for letra in string:
        if not string[0]== " ":
            if letra ==" ":
                espacio+=1
            else:
                palabra+=1
    return espacio


# print("Esta oracion tiene",ObtenerString(input("Escribe una oracion: ")),"espacios")

def solution(number):
    #that function returns the sum of all number that are multiple of 3 or 5
    sum = 0
    i=1
    while i <= number:
        if i % 3 ==0 or i % 5 ==0:
            print(i)
            sum+=1
        i+=1    
  
print(solution(10))