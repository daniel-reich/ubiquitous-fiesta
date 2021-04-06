
def monkey_talk(txt):
    txt = txt.split(' ')
    res = []
    for word in txt:
        if word[0] in 'aeiouAEIOU':res.append('eek')
        else:res.append('OOk')
    return ' '.join(res).capitalize()+'.'

