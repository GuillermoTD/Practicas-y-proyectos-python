
def cipher(text="",s=2):
    Abcdario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    nuevoTexto=""

    for letra in text:
        indice = Abcdario.index(letra)
        nuevoIndice = (indice+2)%26
        nuevoTexto = nuevoTexto + Abcdario[nuevoIndice]
    print(nuevoTexto)

cipher()
