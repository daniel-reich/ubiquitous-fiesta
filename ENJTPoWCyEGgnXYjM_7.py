
def percent_filled(box):
    frase = ''.join(box)
    a = frase.count(' ')
    b = frase.count('o')
    return str(int((b / (a + b)) * 100)) + '%'

