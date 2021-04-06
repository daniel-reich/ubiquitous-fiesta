
def grouping(w):
    a = {}
    for word in w:
        capitals = 0
        for i in word:
            if i.isupper() == True:
                capitals += 1
        if capitals not in a:
            a[capitals] = [word]
        else:
            b = a[capitals]
            b.append(word)
            a[capitals] = b
    for key in a:
        b = a[key]
        b.sort(key=lambda x: x.lower())
        a[key] = b
    return a

