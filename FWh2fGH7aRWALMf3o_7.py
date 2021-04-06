
def cleave(string, lst):
    dicionario, pl, parou, atual, posicao =dict(), [''], [0], 0, 0
    total, maximo = len(string), max([len(i) for i in lst])
    for i in lst: dicionario[i] = True
    while len(pl):
        for letra in range(min(maximo,total-posicao)):
            pl[atual] += string[posicao]; posicao += 1
            if pl[atual] in dicionario:
                if posicao == total: return ' '.join(pl)
                else: parou.append(posicao); pl.append(''); atual += 1; break
        if pl[atual] != '':
            pl.pop(); posicao = parou[atual]; atual -= 1; parou.pop()
    return "Cleaving stalled: Word not found"

