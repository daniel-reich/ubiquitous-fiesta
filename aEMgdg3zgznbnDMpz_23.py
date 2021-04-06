
def rotated_words(txt):
    if len(txt) == 0:
        return 0
    import re
    letters = ["H", "I", "N", "O", "S", "X", "Z","W","*"]
    x = txt.split(' ')
    y = ''
    z = re.sub(' ', '*',txt)
    zogoi = 0
    for i in z:
        if i in letters:
            y += i
    count = y.split('*')
    for i in range(len(set(count))):
        for j in range(len(set(x))):
            if count[i] in set(x) and x[j] in set(count) :
                zogoi += 1
    return zogoi ** 0.5

