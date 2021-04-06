
def countdown(n, txt):
    a = [str(i) + '.' for i in range(n, 0 , -1)]
    texto = ''
    for n in a:
        texto += n + ' '
    return texto + txt.upper() + '!'

