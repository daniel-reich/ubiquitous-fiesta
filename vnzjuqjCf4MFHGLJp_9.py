
def shift_letters(txt, n):
    temptxt = [i for i in txt if i != ' ']
    [temptxt.insert(0, temptxt.pop()) for _ in range(n)]
    [temptxt.insert(i, ' ') for i in [i[0] for i in enumerate(txt) if i[1] == ' ']]
    return ''.join(temptxt)

