
def route_diff(directions):
    txt = ''.join(c for c in sorted(directions, key=lambda x: 'NSEW'.index(x)))
    while 'NS' in txt or 'EW' in txt:
        txt = txt.replace('NS', '').replace('EW', '')
    return len(directions) - len(txt)

