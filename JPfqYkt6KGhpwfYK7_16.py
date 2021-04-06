
def replace_the(txt):
    txt = txt.split()
    for i in range(len(txt)):
        if txt[i].lower() == 'the' and txt[i+1][0] in 'aeiou':
            txt[i] = 'an'
        elif txt[i].lower() == 'the':
            txt[i] = 'a'
    return ' '.join(txt)

