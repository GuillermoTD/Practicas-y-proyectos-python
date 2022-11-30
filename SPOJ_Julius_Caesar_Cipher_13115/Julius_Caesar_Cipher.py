
def cipher(text="KLK"):
    Abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    nuevoTexto = ""

    for letra in text:
        indice = Abecedario.index(letra)
        nuevoIndice = (indice+2) % 26
        nuevoTexto += Abecedario[nuevoIndice]
    print(nuevoTexto)


def deciphered(text="MNM"):
    Abcdario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    nuevoTexto = ""
    for letra in text:
        indice = Abcdario.index(letra)
        nuevoIndice = (indice-2) % 26
        nuevoTexto += Abcdario[nuevoIndice]
    print(nuevoTexto)


# cipher()
# deciphered()

def get_count(string):
    #Return the number (count) of vowels in the given string.
    vowels = ['a','e','i','o','u']
    vowelsCount = 0
    
    for n in string:
        index = vowels.find(n)
        if n == vowels[index]:
            vowelsCount +=1
    print(vowelsCount)


get_count("miralo")
