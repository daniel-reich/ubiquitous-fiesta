
def blah_blah(txt, n):
    words = txt.split()
    blahs = ['blah'] * min(len(words), n)
    return ' '.join(words[:-n] + blahs) + '...'

