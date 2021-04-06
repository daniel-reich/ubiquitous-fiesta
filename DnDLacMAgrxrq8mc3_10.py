
def blah_blah(txt, n):
    sentence = [i for i in txt.split()][:-n]
    blahs = (['blah' for i in range(n)])[:len(txt.split())]
    return ' '.join(sentence + blahs) + '...'

