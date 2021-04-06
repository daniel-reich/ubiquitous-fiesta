
def syllabification(word):
    r=''
    w=word[::-1]
    v='aAeiou'
    while w:
        if w[0] in v:
            r+=w[:2]+'.'
            w=w[2:]
        elif w[0] and w[1] not in v:
            r+=w[:4]+'.'
            w=w[4:]
        else:
            r+=w[:3]+'.'
            w=w[3:]
    return r[::-1].strip('.')

