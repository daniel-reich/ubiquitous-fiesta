
def does_rhyme(txt1, txt2):
    txt1 = txt1.lower()
    txt2 = txt2.lower()
    a = txt1.split(' ')
    b = txt2.split(' ')
    vogais = 'aeiou'
    lista_a = []
    lista_b = []
    for n in vogais:
        if n in a[-1]:
            lista_a.append(n)
        if n in b[-1]:
            lista_b.append(n)
    return lista_a == lista_b

