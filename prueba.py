def capitalizeWord(string):
    oracion = ""
    palabra = ""
    concat = 1
    for letra in string:
        if letra != " ":
            palabra+=letra
            print(palabra)
    
    # palabra.title()
    # print(palabra)
    print(string.capitalize())

    

capitalizeWord("Esto es una oracion donde quiero que cada palabra empieze con mayuscula")
