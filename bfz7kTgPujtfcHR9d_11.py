
def x_pronounce(sentence):
    lst = sentence.split()
    for i, w in enumerate(lst):
        if w == 'x':
            lst[i] = 'ecks'
        elif w[0] == 'x':
            lst[i] = 'z' + w[1:]
        if 'x' in lst[i]:
            lst[i] = w.replace('x', 'cks')
    return ' '.join(lst)

