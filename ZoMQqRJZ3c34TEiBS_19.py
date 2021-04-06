
import string
​
def get_pos(poly, char):
    for i, x in enumerate(poly):
        for j, y in enumerate(x):
            if y == char:
                return (i,j)
​
def playfair(txt, keyword):
    polybius = sorted(list(set(keyword.upper())), key=keyword.upper().index) + [x for x in 'ABCDEFGHIKLMNOPQRSTUVWXYZ' if x not in keyword
    .upper()]
    polybius = [polybius[x:x+5] for x in range(0, 25, 5)]
    
​
    text = txt.upper().translate(str.maketrans('', '', string.punctuation)).replace(' ', '')
    text = [list(text[x:x+2]) for x in range(0, len(text), 2)]
​
    if ' ' in txt:
        a = 0
        while a != len(text):
            if (len(text[a]) == 2) and text[a][0] == text[a][1]:
                text = sum(text, [])
                text.insert(a*2+1, 'X')
                text = [text[x:x+2] for x in range(0, len(text), 2)]
            a += 1
        text = text[:-1] + [[text[-1][0], 'X']] if len(sum(text, [])) % 2 else text
​
    out = ''
    if ' ' in txt:
        for x, y in text:
            row, col = get_pos(polybius, x)
            rowy, coly = get_pos(polybius, y)
​
            if row == rowy:
                out += polybius[row][(col+1)%5] + polybius[row][(coly+1)%5]
            elif coly == col:
                out += polybius[(row+1)%5][col] + polybius[(rowy+1)%5][col]
            else:
                out += polybius[row][coly] + polybius[rowy][col]
    else:
        for x,y in text:
            row, col = get_pos(polybius, x)
            rowy, coly = get_pos(polybius, y)
​
            if row == rowy:
                out += polybius[row][(col-1)%5] + polybius[row][(coly-1)%5]
            elif coly == col:
                out += polybius[(row-1)%5][col] + polybius[(rowy-1)%5][coly]
            else:
                out += polybius[row][coly] + polybius[rowy][col]
    
    return out

