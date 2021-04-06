
def x_pronounce(sentence):
    return ' '.join([word(w) for w in sentence.split()])
​
def word(w):
    if w[0] == 'x':
        if len(w) == 1:
            return 'ecks'
        w = 'z' + w[1:]
    w = w.replace('x', 'cks')
    return w

