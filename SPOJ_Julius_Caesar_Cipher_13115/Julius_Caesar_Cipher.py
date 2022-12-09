
def cipher(text="KLK"):
    Abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                  'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    nuevoTexto = ""

    for letra in text:
        indice = Abecedario.index(letra)
        nuevoIndice = (indice+7) % 26
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

cipher()
# deciphered()
