
def shift_sentence(txt):
    ls=[i for i in txt.split()]
    return ' '.join([ls[i].replace(ls[i][0],ls[i+len(ls)-1][0],1) for i in range(-len(ls),0)])

