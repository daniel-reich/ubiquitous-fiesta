
def sigilize(desire):
    sigil = ''
    for i in reversed(desire):
        if i.lower() not in 'aeiou ' and i not in sigil:
            sigil += i
    return sigil.upper()[::-1]

