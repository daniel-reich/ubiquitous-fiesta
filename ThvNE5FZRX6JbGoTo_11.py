
def inverter(txt, type):
    low = txt.lower().split()
    if type == 'P':
        low[-1] = low[-1].capitalize()
        return ' '.join(low[::-1])
    low = [w[::-1] for w in low]
    low[0] = low[0].capitalize()
    return ' '.join(low)

