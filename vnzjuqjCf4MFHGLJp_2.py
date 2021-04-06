
def shift_letters(txt, n): # right
    ws = [i for i, x in enumerate(txt) if x == ' ']
    lst = [x for x in txt if x != ' ']
    lst = [(x, (i + n) % len(lst)) for i, x in enumerate(lst)]
    lst = sorted(lst, key=lambda x: x[1])
    lst = [x[0] for x in lst]
    for x in ws:
        lst.insert(x, ' ')
    return ''.join(lst)

