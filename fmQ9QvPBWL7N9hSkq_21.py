
def unstretch(word):
    c = ''
    for d in word:
        if c is '':
            c = c + d
        elif c[-1] == d:
           pass
        else:
            c = c + d
    return c

